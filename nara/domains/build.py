from nara.domains.base import ExecutionDomain

class BuildDomain(ExecutionDomain):
    name = "build"
    subdomains = ["make", "cmake", "bazel", "yaml", "json", "toml"]

    def detect(self, intent: str) -> bool:
        return "build" in intent.lower() or "config" in intent.lower()

    def select_subdomain(self, intent: str) -> str:
        return "make"

    def runner(self, subdomain: str) -> str:
        return "build_tool"

    def validator(self):
        return "schema_validation"

    def repair_strategy(self):
        return "graph_fix"
