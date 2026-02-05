# nara/core/repair.py
"""
Enterprise Targeted Repair Engine

Invariant:
- Repairs ONLY the failing component
- Never regenerates whole system
- Stops if patch exceeds bounds
"""

import os

from nara.llm.ollama_client import call_llm
from nara.core.diff_guard import within_bounds


REPAIR_PROMPT = """
You are Nara Repair Engine.

Return ONLY corrected Python code.

Rules:
- Patch only the failing component.
- Preserve unaffected logic.
- Do not rewrite the entire system.

Failure:
{failure}

Code:
{code}
"""


def repair(artifacts: dict, failure: dict):
    failed = failure.get("failed_node")
    if not failed:
        return False

    root = artifacts["root"]
    workspace = os.path.join(root, "workspace")
    target = os.path.join(workspace, f"{failed}.py")

    if not os.path.exists(target):
        return False

    original = open(target, "r", encoding="utf-8").read()

    prompt = REPAIR_PROMPT.format(
        failure=failure,
        code=original,
    )

    patched = call_llm(prompt, name="repair")

    if not within_bounds(original, patched):
        return False

    with open(target, "w", encoding="utf-8") as f:
        f.write(patched)

    return True
