from nara.domains.base import ExecutionDomain

class GPUDomain(ExecutionDomain):
    name = "gpu"
    subdomains = ["cuda", "opencl", "metal"]

    def detect(self, intent: str) -> bool:
        return "gpu" in intent.lower() or "cuda" in intent.lower()

    def select_subdomain(self, intent: str) -> str:
        return "cuda"

    def runner(self, subdomain: str) -> str:
        return "accelerator_runtime"

    def validator(self):
        return "kernel_execution"

    def repair_strategy(self):
        return "limited_manual_repair"
