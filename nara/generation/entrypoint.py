# nara/generation/entrypoint.py
"""
Generates a single deterministic main.py that runs pipeline in order.
"""

def build_main(components: list) -> str:
    lines = []
    lines.append("data = {}")
    lines.append("")

    for c in components:
        mod = c["entrypoint"].replace(".py", "")
        fn = c["name"]

        lines.append(f"from {mod} import run as {fn}")
    lines.append("")
    for c in components:
        lines.append(f"data = {c['name']}(data)")
    lines.append("")
    lines.append('print("PIPELINE_OK", data)')
    return "\n".join(lines)
