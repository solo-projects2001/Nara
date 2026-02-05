import sys
import shutil
import subprocess

REQUIRED_PYTHON = (3, 10)
REQUIRED_MODELS = ["deepseek-coder:6.7b"]

def check_python():
    if sys.version_info < REQUIRED_PYTHON:
        raise RuntimeError("Python 3.10+ required")

def check_ollama():
    if not shutil.which("ollama"):
        raise RuntimeError("Ollama not installed")

    result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
    for model in REQUIRED_MODELS:
        if model not in result.stdout:
            raise RuntimeError(f"Missing Ollama model: {model}")

def main():
    check_python()
    check_ollama()
    print("Nara environment OK")

if __name__ == "__main__":
    main()
