from nara.hybrid.phases import HybridPhase
from nara.hybrid.plan import HybridPlan

def plan_hybrid_flow(intent: str) -> HybridPlan:
    low = intent.lower()

    analysis_terms = ["inspect", "analyze", "validate", "scan"]
    execution_terms = ["apply", "execute", "run", "process"]

    has_analysis = any(t in low for t in analysis_terms)
    has_exec = any(t in low for t in execution_terms)

    if has_analysis and has_exec:
        return HybridPlan(
            phases=[HybridPhase.ANALYZE, HybridPhase.EXECUTE],
            reason="analysis_then_execution_detected",
        )

    if has_analysis:
        return HybridPlan(
            phases=[HybridPhase.ANALYZE],
            reason="analysis_only_detected",
        )

    return HybridPlan(
        phases=[HybridPhase.EXECUTE],
        reason="execution_only_detected",
    )
