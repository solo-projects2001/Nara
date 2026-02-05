from nara.domains.validators.registry import get_validator


def validate(result: dict, artifacts: dict):
    domain = artifacts["domain"]["domain"]

    validator = get_validator(domain)
    return validator.validate(result, artifacts)
