class OverridePolicy:
    """
    Enterprise rule:
    forbidden_domains is the ONLY block list.
    """

    def __init__(self, forbidden_domains=None, require_approval=False):
        self.forbidden_domains = forbidden_domains or []
        self.require_approval = require_approval

    def allowed(self, domain: str) -> bool:
        return domain not in self.forbidden_domains
