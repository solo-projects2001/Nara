class DomainSelection:
    def __init__(self, domain, subdomain):
        self.domain = domain
        self.subdomain = subdomain

    def as_dict(self):
        return {
            "domain": self.domain.name,
            "subdomain": self.subdomain,
        }
