from nara.domains.base import ExecutionDomain

class AIDomain(ExecutionDomain):
    name = "ai"
    subdomains = [
        "pytorch-cpu",
        "tensorflow-cpu",
        "onnx-runtime",
        "llama-cpp",
        "ollama"
    ]

    def detect(self, intent: str) -> bool:
        return "model" in intent.lower() or "ai" in intent.lower()

    def select_subdomain(self, intent: str) -> str:
        return "ollama"

    def runner(self, subdomain: str) -> str:
        return "inference_engine"

    def validator(self):
        return "output_sanity"

    def repair_strategy(self):
        return "prompt_or_config_repair"
