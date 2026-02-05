from nara.composition.interfaces import SystemInterface

def extract_interfaces(structure: dict) -> list[SystemInterface]:
    interfaces = []
    for c in structure.get("components", []):
        contracts = c.get("contracts", {})
        interfaces.append(
            SystemInterface(
                inputs=[contracts.get("input")],
                outputs=[contracts.get("output")]
            )
        )
    return interfaces
