def render_ascii(nodes, edges) -> str:
    lines = []
    for n in nodes:
        lines.append(f"[{n.name}:{n.role}]")

    for e in edges:
        lines.append(f"  {e.source} --> {e.target} ({e.label})")

    return "\n".join(lines)
