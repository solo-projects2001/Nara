from nara.domains.analysis.base import DomainAnalyzer

class ShellAnalyzer(DomainAnalyzer):
    def analyze(self, path: str) -> dict:
        # v1: shell scripts are not statically validated
        return {"ok": True}
