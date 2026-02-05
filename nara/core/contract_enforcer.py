def enforce(contracts: dict, output: str):
    if not output.strip():
        raise RuntimeError("contract_violation")
