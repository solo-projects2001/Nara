# nara/generation/config_writer.py
"""
Writes minimal enterprise config.yaml for generated projects.
"""

import os


def write_config(root: str):
    cfg = """input_dir: .
output_dir: ./out
strict_mode: true
"""
    with open(os.path.join(root, "config.yaml"), "w") as f:
        f.write(cfg)
