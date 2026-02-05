# nara/core/repair_candidates.py
import os

PROMPT_PATH = "nara/llm/prompts/repair_multi.txt"


def generate_candidates(code: str, failure_type: str, k: int = 2):
    """
    Enterprise invariant:
    - Repair must not crash if prompt missing
    - Always returns at least one safe candidate
    """

    if not os.path.exists(PROMPT_PATH):
        # Safe fallback: return original code unchanged
        return [code]

    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        prompt = f.read()

    prompt = prompt.replace("{{FAILURE_TYPE}}", failure_type)
    prompt = prompt.replace("{{CODE}}", code)

    # For now: deterministic single-candidate fallback
    return [code]
