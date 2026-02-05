from nara.domains.base import ExecutionDomain

class VirtualizedDomain(ExecutionDomain):
    name = "virtualized"
    subdomains = ["docker", "podman", "firecracker"]

    def detect(self, intent: str) -> bool:
        return "container" in intent.lower() or "docker" in intent.lower()

    def select_subdomain(self, intent: str) -> str:
        return "docker"

    def runner(self, subdomain: str) -> str:
        return "container_runtime"

    def validator(self):
        return "container_exit"

    def repair_strategy(self):
        return "manifest_repair"
