from nara.domains.scorer import DomainScorer
from nara.domains.confidence import DomainMatch

class ExecutableDomainScorer(DomainScorer):
    def score(self, intent: str) -> DomainMatch | None:
        low = intent.lower()
        keywords = [
            "run", "execute", "process",
            "build", "generate", "produce"
        ]
        hits = [k for k in keywords if k in low]
        if not hits:
            return None

        confidence = min(0.9, 0.3 + 0.1 * len(hits))
        return DomainMatch(
            domain="interpreted",
            subdomain="python",
            confidence=confidence,
            reason=f"execution_keywords:{hits}",
        )
