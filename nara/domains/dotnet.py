from nara.domains.base import ExecutionDomain

class DotNetDomain(ExecutionDomain):
    name = "dotnet"
    subdomains = ["csharp", "fsharp", "vbnet"]

    def detect(self, intent: str) -> bool:
        return "dotnet" in intent.lower() or "c#" in intent.lower()

    def select_subdomain(self, intent: str) -> str:
        return "csharp"

    def runner(self, subdomain: str) -> str:
        return "dotnet_cli"

    def validator(self):
        return "dotnet_exit_contract"

    def repair_strategy(self):
        return "compiler_guided_repair"
