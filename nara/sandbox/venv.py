import subprocess
import os
import sys

def create_venv(path: str):
    subprocess.check_call([sys.executable, "-m", "venv", path])

def pip_install(venv_path: str, package: str):
    pip = os.path.join(venv_path, "Scripts", "pip.exe")
    subprocess.check_call([pip, "install", package])

def python_bin(venv_path: str):
    return os.path.join(venv_path, "Scripts", "python.exe")
