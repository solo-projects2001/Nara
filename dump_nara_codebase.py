import os

ROOT_DIR = "nara"          # project root folder
OUTPUT_FILE = "NARA_FULL_DUMP.txt"

EXCLUDE_DIRS = {
    "__pycache__",
    ".git",
    ".venv",
    "venv",
    "env",
    "node_modules",
    "generated",
}

EXCLUDE_EXTENSIONS = {
    ".pyc",
    ".exe",
    ".dll",
    ".so",
    ".zip",
}

def should_exclude(path: str) -> bool:
    for part in path.split(os.sep):
        if part in EXCLUDE_DIRS:
            return True
    return False

def dump():
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        for root, dirs, files in os.walk(ROOT_DIR):
            if should_exclude(root):
                continue

            for file in files:
                if any(file.endswith(ext) for ext in EXCLUDE_EXTENSIONS):
                    continue

                full_path = os.path.join(root, file)

                try:
                    with open(full_path, "r", encoding="utf-8", errors="replace") as f:
                        content = f.read()
                except Exception as e:
                    content = f"<<FAILED TO READ FILE: {e}>>"

                out.write("\n" + "=" * 80 + "\n")
                out.write(f"FILE: {full_path}\n")
                out.write("=" * 80 + "\n")
                out.write(content)
                out.write("\n")

    print(f"[OK] Full codebase dumped to {OUTPUT_FILE}")

if __name__ == "__main__":
    dump()
