# nara/ux/audit/view.py
from nara.ux.audit.timeline import timeline
from nara.ux.audit.failures import failures

def render_audit():
    lines = ["NARA AUDIT VIEW", "=" * 16, ""]
    lines.append("TIMELINE:")
    for r in timeline()[-20:]:
        lines.append(f"- {r.get('stage')} | {r.get('reason')}")
    lines.append("")
    lines.append("FAILURES:")
    for f in failures()[-10:]:
        lines.append(f"- {f.get('stage')} | {f.get('reason')}")
    return "\n".join(lines)
