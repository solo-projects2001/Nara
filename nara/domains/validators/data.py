from nara.domains.validators.base import DomainValidator

class DataValidator(DomainValidator):
    def validate(self, result: dict):
        if result.get("exit_code", 1) != 0:
            raise RuntimeError("query_execution_failed")
        if not result.get("stdout"):
            raise RuntimeError("empty_query_result")
