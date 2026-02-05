# nara/ux/audit/failures.py
from nara.ux.audit.events import load_events

def failures():
    out = []
    for e in load_events():
        if e.get("stage") in ("execution_failure", "failure"):
            out.append(e)
    return out
