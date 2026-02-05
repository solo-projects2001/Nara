from nara.domains.capabilities import CAPABILITIES

def domain_enabled(domain_name: str) -> bool:
    return (
        domain_name in CAPABILITIES
        and CAPABILITIES[domain_name].get("enabled", False)
    )
