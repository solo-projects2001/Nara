from nara.domains.base import ExecutionDomain

class FunctionalDomain(ExecutionDomain):
    name = "functional"
    subdomains = ["haskell", "ocaml", "lisp", "scheme"]

    def detect(self, intent: str) -> bool:
        return "functional" in intent.lower()

    def select_subdomain(self, intent: str) -> str:
        return "haskell"

    def runner(self, subdomain: str) -> str:
        return "compiler_runtime"

    def validator(self):
        return "type_correctness"

    def repair_strategy(self):
        return "type_error_guided"
