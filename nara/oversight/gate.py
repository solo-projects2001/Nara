class HumanGate:
    def __init__(self, policy):
        self.policy = policy

    def check(self, domain: str) -> bool:
        domain = domain.strip().lower()

        if domain == "analysis":
            return True

        return self.policy.allowed(domain)
