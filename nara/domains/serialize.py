def serialize_domain_match(match) -> dict:
    return {
        "domain": match.domain,
        "subdomain": match.subdomain,
        "confidence": match.confidence,
        "reason": match.reason,
    }
