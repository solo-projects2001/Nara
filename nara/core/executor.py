# nara/core/executor.py
"""
Enterprise Executor

Invariant:
- Always runs workspace/main.py
- Pipeline execution is deterministic
"""

import os
import subprocess


def execute(artifacts: dict) -> dict:
    root = artifacts["root"]
    workspace = os.path.join(root, "workspace")

    entry = os.path.join(workspace, "main.py")

    if not os.path.exists(entry):
        return {"ok": False, "stderr": "missing_main_entrypoint"}

    proc = subprocess.run(
        ["python", "main.py"],
        cwd=workspace,
        capture_output=True,
        text=True,
    )

    return {
        "ok": proc.returncode == 0,
        "exit_code": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
    }
