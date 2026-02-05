from dataclasses import dataclass

@dataclass
class DomainMatch:
    domain: str
    subdomain: str
    confidence: float
    reason: str
