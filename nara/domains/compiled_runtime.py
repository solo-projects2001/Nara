from nara.domains.runtime import DomainRuntime
import os

class CompiledRuntime(DomainRuntime):
    def command(self, subdomain: str, entrypoint: str) -> list[str]:
        binary = entrypoint.replace(".c", "").replace(".rs", "").replace(".go", "")
        return ["./" + binary]
