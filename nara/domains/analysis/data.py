from nara.domains.analysis.base import DomainAnalyzer

class DataAnalyzer(DomainAnalyzer):
    def analyze(self, path: str) -> dict:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()
        if not content:
            return {"ok": False, "type": "empty_query"}
        return {"ok": True}
