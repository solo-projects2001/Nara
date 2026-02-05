from nara.intent.model import IntentClassification, IntentKind
from nara.intent.forbidden import detect_forbidden
from nara.intent.ambiguity import detect_ambiguity

def classify_intent(intent: str) -> IntentClassification:
    if detect_forbidden(intent):
        return IntentClassification(
            kind=IntentKind.FORBIDDEN,
            reason="forbidden_pattern_detected",
            confidence=1.0,
        )

    ambiguities = detect_ambiguity(intent)
    if ambiguities:
        return IntentClassification(
            kind=IntentKind.AMBIGUOUS,
            reason=f"ambiguous_terms: {ambiguities}",
            confidence=0.4,
        )

    low = intent.lower()

    analysis_keywords = [
        "inspect", "analyze", "audit", "scan",
        "classify", "inventory", "detect", "report",
    ]
    exec_keywords = [
        "run", "execute", "process", "generate",
        "build", "produce", "create pipeline",
    ]

    is_analysis = any(k in low for k in analysis_keywords)
    is_exec = any(k in low for k in exec_keywords)

    if is_analysis and is_exec:
        return IntentClassification(
            kind=IntentKind.HYBRID,
            reason="analysis_and_execution_keywords",
            confidence=0.8,
        )

    if is_analysis:
        return IntentClassification(
            kind=IntentKind.ANALYSIS,
            reason="analysis_keywords_detected",
            confidence=0.9,
        )

    return IntentClassification(
        kind=IntentKind.EXECUTABLE,
        reason="execution_keywords_detected",
        confidence=0.9,
    )
