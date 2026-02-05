import json

from nara.llm.ollama_client import call_llm
from nara.intent.classifier import classify_intent
from nara.intent.model import IntentKind
from nara.system.resolve import resolve_system_type
from nara.domains.resolve import select_domain


PROMPT = """
Return ONLY JSON.

{
  "system_type": "python_script | pipeline | multi_component",
  "components": []
}

Intent:
{{INTENT}}
"""


def parse_intent(raw: str) -> dict:
    return {"raw": raw.strip()}


def infer_structure(intent_obj: dict) -> dict:
    """
    Enterprise invariant:
    - _intent is always a dict
    - domain always has a safe fallback
    - never returns inconsistent domain objects
    """

    raw_intent = intent_obj["raw"]

    # Intent classification
    intent_cls = classify_intent(raw_intent)

    if intent_cls.kind == IntentKind.FORBIDDEN:
        raise RuntimeError(f"forbidden_intent: {intent_cls.reason}")

    # Domain selection (deterministic fallback)
    domain_sel = select_domain(intent_obj)
    domain_name = domain_sel.get("domain") or "interpreted"

    # System type selection
    system_decl = resolve_system_type(raw_intent)

    # LLM structural shell (optional)
    raw = call_llm(PROMPT.replace("{{INTENT}}", raw_intent), name="intent")
    structure = json.loads(raw)

    # HARD NORMALIZATION
    structure["_intent"] = intent_obj
    structure["_intent_classification"] = {
        "kind": intent_cls.kind.value,
        "reason": intent_cls.reason,
        "confidence": intent_cls.confidence,
    }

    structure["_system"] = {
        "type": system_decl.system_type.value,
        "reason": system_decl.reason,
    }

    structure["_domain"] = {
    "domain": domain_name,
    "subdomain": domain_sel.get("subdomain", "python"),
    "confidence": domain_sel.get("confidence", 0.6),
  }


    structure.setdefault("components", [])

    return structure
