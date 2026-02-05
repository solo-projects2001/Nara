# nara/ux/artifacts/view.py
from nara.ux.artifacts.browser import list_runs, list_files

def render_artifacts():
    lines = ["NARA ARTIFACT BROWSER", "=" * 22]
    for r in list_runs()[-5:]:
        lines.append(f"\nRUN {r}:")
        for f in list_files(r):
            lines.append(f"  - {f}")
    return "\n".join(lines)
