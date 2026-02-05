import ast
from nara.domains.analysis.base import DomainAnalyzer

class InterpretedAnalyzer(DomainAnalyzer):
    def analyze(self, path: str) -> dict:
        if path.endswith(".py"):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    ast.parse(f.read())
                return {"ok": True}
            except SyntaxError as e:
                return {"ok": False, "type": "syntax_error", "detail": str(e)}
        return {"ok": True}
