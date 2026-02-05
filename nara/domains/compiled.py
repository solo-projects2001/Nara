from nara.domains.base import ExecutionDomain

class CompiledDomain(ExecutionDomain):
    name = "compiled"
    subdomains = [
        "c",
        "cpp",
        "rust",
        "go",
        "zig",
        "nim",
        "d"
    ]

    def detect(self, intent: str) -> bool:
        return any(k in intent.lower() for k in ["compile", "binary", "rust", "c++", "go"])

    def select_subdomain(self, intent: str) -> str:
        if "rust" in intent.lower():
            return "rust"
        return "c"

    def runner(self, subdomain: str) -> str:
        return "compile_then_execute"

    def validator(self):
        return "binary_exit_code"

    def repair_strategy(self):
        return "compiler_error_repair"
