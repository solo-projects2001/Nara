# nara/domains/validators/analysis.py

class AnalysisValidator:
    """
    Analysis domain is inspection-only.

    Validation rule:
    - Always succeed unless explicitly unsafe.
    """

    def validate(self, result: dict, artifacts: dict):
        return True
