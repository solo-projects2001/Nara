# nara/ux/artifacts/browser.py
import os

BASE = "generated/projects"

def list_runs():
    if not os.path.isdir(BASE):
        return []
    return sorted(os.listdir(BASE))

def list_files(run_id):
    root = os.path.join(BASE, run_id)
    files = []
    for r, _, fs in os.walk(root):
        for f in fs:
            files.append(os.path.relpath(os.path.join(r, f), root))
    return files
