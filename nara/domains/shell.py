from nara.domains.base import ExecutionDomain

class ShellDomain(ExecutionDomain):
    name = "shell"
    subdomains = ["bash", "zsh", "powershell", "batch"]

    def detect(self, intent: str) -> bool:
        return "shell" in intent.lower() or "bash" in intent.lower()

    def select_subdomain(self, intent: str) -> str:
        return "bash"

    def runner(self, subdomain: str) -> str:
        return "shell_exec"

    def validator(self):
        return "exit_code"

    def repair_strategy(self):
        return "command_rewrite"
