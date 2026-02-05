def file_provenance(component: dict) -> dict:
    return {
        "generated_for": component["name"],
        "role": component["role"],
        "contracts": component["contracts"],
    }
