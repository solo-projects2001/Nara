from nara.ux.identity import describe

def whoami() -> str:
    ident = describe()
    lines = [
        f"Name: {ident['name']}",
        f"Type: {ident['type']} ({ident['layer']} layer)",
        "",
        "Purpose:",
    ]
    for p in ident["purpose"]:
        lines.append(f"  - {p}")

    lines.append("")
    lines.append("Explicitly NOT:")
    for n in ident["explicit_non_goals"]:
        lines.append(f"  - {n}")

    lines.append("")
    lines.append("Guarantees:")
    for g in ident["guarantees"]:
        lines.append(f"  - {g}")

    return "\n".join(lines)
