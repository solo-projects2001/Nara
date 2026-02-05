# nara/contracts/builder.py
from nara.contracts.schema import ContractSchema

def build_contract(role: str) -> dict:
    """
    GEN-3: Role-specific contract synthesis.
    """
    if "scanner" in role:
        return ContractSchema(input_type="path", output_type="findings").dict()

    if "validator" in role:
        return ContractSchema(input_type="records", output_type="validated").dict()

    if "report" in role or "export" in role:
        return ContractSchema(input_type="metrics", output_type="report").dict()

    return ContractSchema(input_type="json", output_type="json").dict()
