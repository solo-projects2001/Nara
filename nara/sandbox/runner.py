import subprocess
import shutil

def run_in_sandbox(sandbox: dict, command: list[str]):
    policy = sandbox["policy"]

    executable = command[0]
    if shutil.which(executable) is None:
        return {
            "success": False,
            "stderr": f"tool_not_available: {executable}",
            "exit_code": 127
        }

    proc = subprocess.run(
        command,
        cwd=sandbox["workspace"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    return {
        "success": proc.returncode == 0,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "exit_code": proc.returncode
    }
