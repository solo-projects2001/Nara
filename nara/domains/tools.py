from nara.domains.base import ExecutionDomain

class ToolDomain(ExecutionDomain):
    name = "tools"
    subdomains = ["ffmpeg", "imagemagick", "curl", "radare2"]

    def detect(self, intent: str) -> bool:
        return "tool" in intent.lower() or "binary" in intent.lower()

    def select_subdomain(self, intent: str) -> str:
        return "ffmpeg"

    def runner(self, subdomain: str) -> str:
        return "cli_tool"

    def validator(self):
        return "exit_code"

    def repair_strategy(self):
        return "argument_rewrite"
