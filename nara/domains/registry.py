# nara/domains/registry.py

def resolve_domain(intent: str) -> dict:
    low = intent.lower()

    wants_execution = any(
        k in low for k in [
            "pipeline", "ingest", "process", "execute",
            "tail", "monitor", "aggregate", "export",
            "generate", "runner", "system"
        ]
    )

    wants_analysis_only = any(
        k in low for k in [
            "inspect", "audit", "scan", "compliance"
        ]
    )

    # ✅ If execution is needed → interpreted always wins
    if wants_execution:
        return {"domain": "interpreted", "confidence": 0.85}

    # ✅ Pure inspection only → analysis
    if wants_analysis_only:
        return {"domain": "analysis", "confidence": 0.9}

    # Data query domain
    if any(k in low for k in ["sql", "query", "database"]):
        return {"domain": "data", "confidence": 0.8}

    # Default safe fallback
    return {"domain": "interpreted", "confidence": 0.6}
