from nara.domains.repairs.base import DomainRepair
from nara.core.repair_candidates import generate_candidates

class DataRepair(DomainRepair):
    def repair(self, artifacts: dict, failure: dict) -> bool:
        path = list(artifacts["files"].values())[0]
        with open(path) as f:
            query = f.read()

        candidates = generate_candidates(query, "query_error", 1)
        if not candidates:
            return False

        with open(path, "w") as f:
            f.write(candidates[0])
        return True
