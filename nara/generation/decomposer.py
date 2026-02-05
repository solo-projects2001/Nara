# nara/generation/decomposer.py

def _select_blueprint(intent: str) -> str:
    low = intent.lower()

    if "compliance" in low or "inspect" in low or "configuration" in low:
        return "compliance_scanner"
    if "log" in low or "monitor" in low:
        return "log_monitoring"
    if "csv" in low or "etl" in low or "pipeline" in low:
        return "etl_pipeline"
    if "benchmark" in low or "evaluate" in low:
        return "benchmark_runner"
    if "tool" in low or "harness" in low:
        return "tool_harness"
    if "report" in low:
        return "report_system"

    return "default"


def _roles_for_blueprint(bp: str):
    return {
        "etl_pipeline": ["ingestor", "validator", "aggregator", "reporter"],
        "compliance_scanner": ["scanner", "rule_engine", "findings_export"],
        "log_monitoring": ["tailer", "parser", "metrics", "alert_report"],
        "tool_harness": ["adapter", "runner", "collector"],
        "benchmark_runner": ["suite_loader", "executor", "scoreboard"],
        "report_system": ["loader", "formatter", "exporter"],
        "default": ["loader", "processor", "reporter"],
    }[bp]


def _build_contract(role: str):
    if "scanner" in role:
        return {"input": "path", "output": "findings"}
    if "validator" in role:
        return {"input": "records", "output": "validated"}
    if "report" in role or "export" in role:
        return {"input": "metrics", "output": "report"}
    return {"input": "json", "output": "json"}


def decompose(structure: dict):
    # Support both formats:
    # structure["_intent"] may be dict or string
    raw_intent = structure.get("_intent")

    if isinstance(raw_intent, dict):
        intent_text = raw_intent.get("raw", "")
    else:
        intent_text = str(raw_intent)

    blueprint = _select_blueprint(intent_text)

    # Ensure _system exists
    structure.setdefault("_system", {})
    structure["_system"]["blueprint"] = blueprint

    roles = _roles_for_blueprint(blueprint)

    components = []
    for role in roles:
        components.append(
            {
                "name": role,
                "role": role,
                "entrypoint": f"{role}.py",
                "contracts": _build_contract(role),
            }
        )

    return components
