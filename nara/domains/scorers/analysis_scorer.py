from nara.domains.scorer import DomainScorer
from nara.domains.confidence import DomainMatch

class AnalysisDomainScorer(DomainScorer):
    def score(self, intent: str) -> DomainMatch | None:
        low = intent.lower()
        keywords = [
            "inspect", "analyze", "audit", "scan",
            "classify", "inventory", "detect", "report"
        ]
        hits = [k for k in keywords if k in low]
        if not hits:
            return None

        confidence = min(0.9, 0.2 + 0.1 * len(hits))
        return DomainMatch(
            domain="analysis",
            subdomain="static",
            confidence=confidence,
            reason=f"analysis_keywords:{hits}",
        )
