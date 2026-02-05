# nara/ux/export/bundle.py
"""
Enterprise Bundle Export

Returns the bundle path for a run directory.
"""

import os
import zipfile


def export_run(run_id: str):
    root = os.path.join("generated", "projects", run_id)
    bundle = os.path.join(root, "bundle.zip")

    with zipfile.ZipFile(bundle, "w", zipfile.ZIP_DEFLATED) as z:
        for r, _, fs in os.walk(root):
            for f in fs:
                fp = os.path.join(r, f)
                z.write(fp, arcname=os.path.relpath(fp, root))

    return bundle
