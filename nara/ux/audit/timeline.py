# nara/ux/audit/timeline.py
from nara.ux.audit.events import load_events

def timeline():
    rows = []
    for e in load_events():
        rows.append({
            "stage": e.get("stage"),
            "reason": e.get("reason"),
            "ts": e.get("ts", ""),
        })
    return rows
