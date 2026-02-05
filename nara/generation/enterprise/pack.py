# nara/generation/enterprise/pack.py
import os
import zipfile

def bundle_project(root: str):
    out = os.path.join(root, "bundle.zip")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for r, _, fs in os.walk(root):
            for f in fs:
                fp = os.path.join(r, f)
                z.write(fp, arcname=os.path.relpath(fp, root))
    return out
