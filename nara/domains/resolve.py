from nara.domains.registry import resolve_domain

def select_domain(intent: dict) -> dict:
    raw = intent.get("raw") if isinstance(intent, dict) else str(intent)

    sel = resolve_domain(raw)

    # Enterprise fallback
    return {
        "domain": sel.get("domain", "interpreted"),
        "subdomain": sel.get("subdomain", "python"),
        "confidence": sel.get("confidence", 0.6),
    }
