from nara.domains.base import ExecutionDomain

class InterpretedDomain(ExecutionDomain):
    name = "interpreted"
    subdomains = [
        "python-cpython",
        "python-pypy",
        "javascript-node",
        "javascript-deno",
        "javascript-bun",
        "ruby-mri",
        "lua",
        "php",
        "perl",
        "r"
    ]

    def detect(self, intent: str) -> bool:
        return any(k in intent.lower() for k in ["python", "script", "javascript", "node"])

    def select_subdomain(self, intent: str) -> str:
        if "javascript" in intent.lower():
            return "javascript-node"
        return "python-cpython"

    def runner(self, subdomain: str) -> str:
        return "interpreter"

    def validator(self):
        return "stdout_contract"

    def repair_strategy(self):
        return "line_level_repair"
