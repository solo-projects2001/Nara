# nara/generation/languages/scaffold.py
import os

def scaffold_language(root: str, lang: str):
    """
    GEN-4: Domain-specific skeleton roots.
    """
    if lang == "sql":
        os.makedirs(os.path.join(root, "sql"), exist_ok=True)

    if lang == "javascript":
        os.makedirs(os.path.join(root, "js"), exist_ok=True)

    if lang == "rust":
        os.makedirs(os.path.join(root, "rust"), exist_ok=True)
