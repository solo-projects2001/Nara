from nara.domains.runtime import DomainRuntime

class ShellRuntime(DomainRuntime):
    def command(self, subdomain: str, entrypoint: str) -> list[str]:
        if subdomain == "bash":
            return ["bash", entrypoint]
        if subdomain == "powershell":
            return ["pwsh", "-File", entrypoint]
        if subdomain == "batch":
            return ["cmd", "/c", entrypoint]

        raise RuntimeError("unsupported_shell_subdomain")
