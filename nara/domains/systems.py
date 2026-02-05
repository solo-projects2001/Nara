from nara.domains.base import ExecutionDomain

class SystemsDomain(ExecutionDomain):
    name = "systems"
    subdomains = ["assembly", "wasm", "embedded"]

    def detect(self, intent: str) -> bool:
        return any(k in intent.lower() for k in ["wasm", "embedded", "assembly"])

    def select_subdomain(self, intent: str) -> str:
        return "wasm"

    def runner(self, subdomain: str) -> str:
        return "toolchain"

    def validator(self):
        return "artifact_validation"

    def repair_strategy(self):
        return "limited_manual_repair"
