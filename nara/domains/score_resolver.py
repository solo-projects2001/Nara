from nara.domains.scorers.analysis_scorer import AnalysisDomainScorer
from nara.domains.scorers.executable_scorer import ExecutableDomainScorer

SCORERS = [
    AnalysisDomainScorer(),
    ExecutableDomainScorer(),
]

def resolve_by_score(intent: str):
    matches = []
    for scorer in SCORERS:
        m = scorer.score(intent)
        if m:
            matches.append(m)

    if not matches:
        return None

    matches.sort(key=lambda m: m.confidence, reverse=True)
    return matches
