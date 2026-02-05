# nara/generation/templates.py
"""
Enterprise Role Templates (State-Chaining Enabled)

Invariant:
- Every component reads/writes _state.json
- Pipeline becomes real deterministic transformation
- No duplicated template blocks
- No game/example domains
"""

STATE_WRAPPER = """\
import json

def run(state: dict) -> dict:
{BODY}

if __name__ == "__main__":
    state = json.load(open("_state.json", "r", encoding="utf-8"))
    state = run(state)
    json.dump(state, open("_state.json", "w", encoding="utf-8"), indent=2)
"""


def wrap(body: str) -> str:
    body_lines = body.strip().splitlines()
    indented = "\n".join("    " + line for line in body_lines)
    return STATE_WRAPPER.replace("{BODY}", indented)


TEMPLATES = {
    # --- Compliance Blueprint ---
    "scanner": wrap("""\
import os

root = state.get("root", ".")

configs = []
for dirpath, _, files in os.walk(root):
    for f in files:
        if f.endswith((".json", ".yaml", ".yml")):
            configs.append(os.path.join(dirpath, f))

state["configs_found"] = configs
return state
"""),

    "rule_engine": wrap("""\
findings = []
for path in state.get("configs_found", []):
    findings.append({"file": path, "status": "unchecked"})

state["findings"] = findings
return state
"""),

    "findings_export": wrap("""\
import json, os

os.makedirs("out", exist_ok=True)
out_path = os.path.join("out", "findings.json")

with open(out_path, "w", encoding="utf-8") as f:
    json.dump({"findings": state.get("findings", [])}, f, indent=2)

state["report_path"] = out_path
return state
"""),

    # --- Log Monitoring Blueprint ---
    "tailer": wrap("""\
lines = ["example log line", "another log line"]
state["log_lines"] = lines
return state
"""),

    "parser": wrap("""\
parsed = [{"raw": line, "level": "INFO"} for line in state.get("log_lines", [])]
state["parsed_events"] = parsed
return state
"""),

    "metrics": wrap("""\
count = len(state.get("parsed_events", []))
state["metrics"] = {"event_count": count}
return state
"""),

    "alert_report": wrap("""\
import json, os

os.makedirs("out", exist_ok=True)
out_path = os.path.join("out", "metrics.json")

with open(out_path, "w", encoding="utf-8") as f:
    json.dump(state.get("metrics", {}), f, indent=2)

state["metrics_path"] = out_path
return state
"""),
}
