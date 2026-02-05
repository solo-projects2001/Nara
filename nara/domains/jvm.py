from nara.domains.base import ExecutionDomain

class JVMDomain(ExecutionDomain):
    name = "jvm"
    subdomains = ["java", "kotlin", "scala", "clojure", "groovy"]

    def detect(self, intent: str) -> bool:
        return "jvm" in intent.lower() or "java" in intent.lower()

    def select_subdomain(self, intent: str) -> str:
        return "java"

    def runner(self, subdomain: str) -> str:
        return "jvm_runtime"

    def validator(self):
        return "jvm_exit_contract"

    def repair_strategy(self):
        return "compiler_guided_repair"
