class ContractViolation(Exception):
    def __init__(self, kind: str, description: str):
        super().__init__(f"{kind}_violation: {description}")
        self.kind = kind
        self.description = description
