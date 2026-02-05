from nara.domains.base import ExecutionDomain

class ScientificDomain(ExecutionDomain):
    name = "scientific"
    subdomains = ["matlab", "octave", "julia", "fortran"]

    def detect(self, intent: str) -> bool:
        return "scientific" in intent.lower() or "numeric" in intent.lower()

    def select_subdomain(self, intent: str) -> str:
        return "julia"

    def runner(self, subdomain: str) -> str:
        return "numeric_runtime"

    def validator(self):
        return "numeric_tolerance"

    def repair_strategy(self):
        return "expression_repair"
