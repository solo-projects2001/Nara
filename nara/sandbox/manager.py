import os
import uuid
from nara.domains.sandbox_resolver import get_policy

BASE = "generated/sandboxes"

def create_sandbox(domain: str):
    run_id = str(uuid.uuid4())
    root = os.path.join(BASE, run_id)
    workspace = os.path.join(root, "workspace")
    os.makedirs(workspace, exist_ok=True)

    return {
        "run_id": run_id,
        "root": root,
        "workspace": workspace,
        "policy": get_policy(domain)
    }
