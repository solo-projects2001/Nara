def validate_domain(domain, subdomain: str):
    if subdomain not in domain.subdomains:
        raise RuntimeError("invalid_subdomain_for_domain")
