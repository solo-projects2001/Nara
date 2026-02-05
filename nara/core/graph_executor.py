# nara/core/graph_executor.py
"""
Enterprise Graph Executor (Deterministic Data Chaining)

Guarantees:
- Executes nodes in pipeline order
- Passes state.json between components
- failed_node attribution is exact
- Validator-compatible exit_code/stdout/stderr
"""

import os
import json
import subprocess


STATE_FILE = "_state.json"


def _load_state(workspace: str) -> dict:
    path = os.path.join(workspace, STATE_FILE)
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_state(workspace: str, state: dict):
    path = os.path.join(workspace, STATE_FILE)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)


def run_graph(graph: dict, artifacts: dict):
    root = artifacts["root"]
    workspace = os.path.join(root, "workspace")

    nodes = graph.get("nodes", [])
    if not nodes:
        return False, None, {
            "exit_code": 1,
            "stdout": "",
            "stderr": "empty_pipeline",
        }

    # Initialize deterministic state
    _save_state(workspace, {})

    combined_out = []
    combined_err = []

    for node in nodes:
        name = node["id"]
        file_path = os.path.join(workspace, f"{name}.py")

        if not os.path.exists(file_path):
            return False, name, {
                "exit_code": 1,
                "stdout": "",
                "stderr": f"missing_component_file: {name}.py",
            }

        # Run node as subprocess
        proc = subprocess.run(
            ["python", f"{name}.py"],
            cwd=workspace,
            capture_output=True,
            text=True,
        )

        combined_out.append(proc.stdout)
        combined_err.append(proc.stderr)

        if proc.returncode != 0:
            return False, name, {
                "exit_code": proc.returncode,
                "stdout": proc.stdout,
                "stderr": proc.stderr,
            }

        # After node execution, enforce state continuity
        state = _load_state(workspace)
        if not isinstance(state, dict):
            return False, name, {
                "exit_code": 1,
                "stdout": proc.stdout,
                "stderr": "state_corruption: not a dict",
            }

    # SUCCESS
    return True, None, {
        "exit_code": 0,
        "stdout": "\n".join(combined_out),
        "stderr": "\n".join(combined_err),
    }
