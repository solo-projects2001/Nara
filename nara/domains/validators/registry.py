# nara/domains/validators/registry.py

from nara.domains.validators.interpreted import InterpretedValidator
from nara.domains.validators.compiled import CompiledValidator
from nara.domains.validators.shell import ShellValidator
from nara.domains.validators.data import DataValidator
from nara.domains.validators.analysis import AnalysisValidator


VALIDATORS = {
    "interpreted": InterpretedValidator(),
    "compiled": CompiledValidator(),
    "shell": ShellValidator(),
    "data": DataValidator(),
    "analysis": AnalysisValidator(),
}


def get_validator(domain_name: str):
    domain = domain_name.strip().lower()

    if domain not in VALIDATORS:
        raise RuntimeError(f"no_validator_for_domain: {domain}")

    return VALIDATORS[domain]
