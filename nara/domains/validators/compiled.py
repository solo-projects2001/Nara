from nara.domains.validators.base import DomainValidator

class CompiledValidator(DomainValidator):
    def validate(self, result: dict):
        if result.get("exit_code", 1) != 0:
            raise RuntimeError("compiled_execution_error")
