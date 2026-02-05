class AnalysisDomain:
    name = "analysis"

    def detect(self, intent: str) -> bool:
        low = intent.lower()
        keys = ["inspect", "analyze", "audit", "scan", "report", "compliance"]
        return any(k in low for k in keys)

    def select_subdomain(self, _intent: str) -> str:
        """
        Subdomain is static for now.
        _intent means intentionally unused.
        """
        return "inspection"
