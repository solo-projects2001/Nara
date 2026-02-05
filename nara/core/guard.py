from nara.core.intent_guard import IntentRejected


ALLOWED_DOMAINS = {
    "analysis",
    "interpreted",
    "data",
    "shell",
}


def guard_intent(intent: str, domain_name: str):
    """
    Enterprise invariant:
    - Guard enforces only true forbidden domains
    - Analysis must ALWAYS be allowed
    - domain_disabled must never trigger for valid domains
    """

    domain = domain_name.strip().lower()

    # Always allow analysis
    if domain == "analysis":
        return

    # Block only unknown domains
    if domain not in ALLOWED_DOMAINS:
        raise IntentRejected(f"domain_disabled: {domain}")

    return
