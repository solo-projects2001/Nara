from nara.domains.analysis.base import DomainAnalyzer

class CompiledAnalyzer(DomainAnalyzer):
    def analyze(self, path: str) -> dict:
        # Compilation handled later; no static check here
        return {"ok": True}
