from nara.domains.validators.base import DomainValidator

class ShellValidator(DomainValidator):
    def validate(self, result: dict):
        if result.get("exit_code", 1) != 0:
            raise RuntimeError("shell_command_failed")
