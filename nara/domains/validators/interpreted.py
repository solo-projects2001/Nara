# nara/domains/validators/interpreted.py

from nara.domains.validators.base import DomainValidator


class InterpretedValidator(DomainValidator):
    """
    Validator for interpreted execution (Python).

    Contract:
    - exit_code must be 0
    - ok must be True
    """

    def validate(self, result: dict, artifacts: dict):
        if result.get("exit_code", 1) != 0:
            raise RuntimeError(
                f"interpreted_runtime_error: {result.get('stderr','')}"
            )

        if not result.get("ok", True):
            raise RuntimeError("interpreted_validation_failed")

        return True
