# nara/core/loop.py
"""
Nara Core Execution Loop (Enterprise Stable)

Flow:
intent → structure → artifacts → execute → classify → repair → validate
"""

from nara.core.intent import parse_intent, infer_structure
from nara.core.planner import plan
from nara.core.artifacts import generate_artifacts
from nara.core.graph_executor import run_graph
from nara.core.classifier import classify
from nara.core.repair import repair
from nara.core.validator import validate

from nara.policy.budget import Budget
from nara.policy.limits import MAX_REPAIRS

from nara.core.intent_guard import guard_intent, IntentRejected

from nara.oversight.policy import OverridePolicy
from nara.oversight.gate import HumanGate
from nara.oversight.log import log_decision


def run(raw_intent: str):
    """
    Single deterministic control loop.
    """

    # 1. Guard intent
    try:
        guard_intent(raw_intent)
    except IntentRejected as e:
        return {"status": "rejected", "reason": str(e)}

    # 2. Parse + infer structure
    intent_obj = parse_intent(raw_intent)
    structure = infer_structure(intent_obj)

    # 3. Domain policy gate
    policy = OverridePolicy(
        forbidden_domains=["jvm", "build", "virtualized"],
        require_approval=False,
    )
    gate = HumanGate(policy)

    domain = structure["_domain"]["domain"].strip().lower()
    structure["_domain"]["domain"] = domain

    if not gate.check(domain):
        return {"status": "rejected", "reason": f"domain_disabled: {domain}"}

    log_decision("intent", {"intent": raw_intent, "domain": domain})

    # 4. Plan
    plan(structure)
    log_decision("plan", {"blueprint": structure["_system"].get("blueprint")})

    # 5. Generate artifacts
    artifacts = generate_artifacts(structure)
    log_decision("artifacts", {"root": artifacts["root"]})

    graph = artifacts["graph"]

    # 6. Execute + Repair loop
    budget = Budget(MAX_REPAIRS, 30)

    while True:
        ok, failed_node, result = run_graph(graph, artifacts)
        if not ok:
            print("EXECUTION_FAILED:", result.get("stderr"))
            print("FAILED_NODE:", failed_node)

        if ok:
            validate(result, artifacts)
            log_decision("success", result)
            return {"status": "success"}

        log_decision(
            "execution_failure",
            {"failed_node": failed_node, "error": str(result)},
        )

        failure = classify(result, artifacts)

        if budget.exhausted():
            return {"status": "stopped", "reason": "budget_exhausted"}

        repaired = repair(artifacts, failure)

        if not repaired:
            return {"status": "stopped", "reason": "irreparable"}

        budget.repair_used()
