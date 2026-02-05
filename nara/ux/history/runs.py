# nara/ux/history/runs.py
import os

BASE = "generated/projects"

def list_runs():
    if not os.path.isdir(BASE):
        return []
    return sorted(os.listdir(BASE))
