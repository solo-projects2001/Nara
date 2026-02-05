from nara.domains.repairs.base import DomainRepair
from nara.core.repair_candidates import generate_candidates

class InterpretedRepair(DomainRepair):
    def repair(self, artifacts: dict, failure: dict) -> bool:
        path = list(artifacts["files"].values())[0]
        with open(path) as f:
            code = f.read()

        candidates = generate_candidates(code, failure["type"], 2)
        if not candidates:
            return False

        with open(path, "w") as f:
            f.write(candidates[0] + "\n")
        return True
