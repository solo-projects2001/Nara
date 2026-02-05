from nara.domains.repairs.base import DomainRepair

class CompiledRepair(DomainRepair):
    def repair(self, artifacts: dict, failure: dict) -> bool:
        # v1: cannot auto-repair compiled sources safely
        return False
