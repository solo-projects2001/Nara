from nara.domains.sandbox_policies import POLICIES

def get_policy(domain_name: str):
    if domain_name not in POLICIES:
        raise RuntimeError(f"no_sandbox_policy_for_domain: {domain_name}")
    return POLICIES[domain_name]
