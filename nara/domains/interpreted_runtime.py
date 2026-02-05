from nara.domains.runtime import DomainRuntime

class InterpretedRuntime(DomainRuntime):
    def command(self, subdomain: str, entrypoint: str) -> list[str]:
        if subdomain.startswith("python"):
            return ["python", entrypoint]
        if subdomain.startswith("javascript-node"):
            return ["node", entrypoint]
        if subdomain.startswith("javascript-deno"):
            return ["deno", "run", entrypoint]
        if subdomain.startswith("javascript-bun"):
            return ["bun", entrypoint]
        if subdomain.startswith("ruby"):
            return ["ruby", entrypoint]
        if subdomain == "lua":
            return ["lua", entrypoint]
        if subdomain == "php":
            return ["php", entrypoint]
        if subdomain == "perl":
            return ["perl", entrypoint]
        if subdomain == "r":
            return ["Rscript", entrypoint]

        raise RuntimeError("unsupported_interpreted_subdomain")
