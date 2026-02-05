from nara.domains.repairs.interpreted import InterpretedRepair
from nara.domains.repairs.compiled import CompiledRepair
from nara.domains.repairs.shell import ShellRepair
from nara.domains.repairs.data import DataRepair

REPAIRS = {
    "interpreted": InterpretedRepair(),
    "compiled": CompiledRepair(),
    "shell": ShellRepair(),
    "data": DataRepair(),
}

def get_repair(domain_name: str):
    if domain_name not in REPAIRS:
        raise RuntimeError(f"no_repair_for_domain: {domain_name}")
    return REPAIRS[domain_name]
