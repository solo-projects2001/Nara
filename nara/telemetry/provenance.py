import json, uuid, os

BASE = "generated/projects/demo/provenance.jsonl"

def node(kind: str, payload: dict) -> str:
    os.makedirs(os.path.dirname(BASE), exist_ok=True)
    nid = str(uuid.uuid4())
    with open(BASE, "a") as f:
        f.write(json.dumps({"id": nid, "kind": kind, "payload": payload}) + "\n")
    return nid

def edge(src: str, dst: str, label: str):
    with open(BASE, "a") as f:
        f.write(json.dumps({"edge": [src, dst], "label": label}) + "\n")
