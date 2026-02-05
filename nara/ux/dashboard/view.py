from nara.ux.dashboard.summary import load_events

def render_dashboard():
    events = load_events()
    lines = ["NARA OPERATOR DASHBOARD", "=" * 25]

    for e in events[-20:]:
        stage = e.get("stage")
        reason = e.get("reason", "")
        lines.append(f"- {stage}: {reason}")

    return "\n".join(lines)
