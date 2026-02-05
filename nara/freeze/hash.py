import hashlib
import os

def hash_directory(path: str) -> str:
    h = hashlib.sha256()
    for root, _, files in os.walk(path):
        for f in sorted(files):
            fp = os.path.join(root, f)
            with open(fp, "rb") as fh:
                h.update(fh.read())
    return h.hexdigest()
