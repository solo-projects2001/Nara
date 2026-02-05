def scaffold_main(components: list[dict], wiring: dict) -> str:
    lines = ["from typing import Any\n"]
    for c in components:
        lines.append(f"import {c['entrypoint'].replace('.py','')}\n")

    lines.append("\ndef main():\n")
    lines.append("    data = None\n")
    for c in components:
        mod = c["entrypoint"].replace(".py", "")
        lines.append(f"    data = {mod}.run(data)\n")

    lines.append("\nif __name__ == '__main__':\n    main()\n")
    return "".join(lines)
