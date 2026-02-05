from nara.contracts.defaults import default_contract
from nara.composition.extract import extract_interfaces
from nara.composition.compatibility import check_compatibility
from nara.system.guard import validate_system_type
from nara.system.types import SystemType

def plan(structure: dict):
    domain = structure["_domain"]["domain"]
    system_type = structure["_system"]["type"]

    validate_system_type(SystemType(system_type), domain)

    interfaces = extract_interfaces(structure)
    if interfaces and not check_compatibility(interfaces):
        raise RuntimeError("system_interface_incompatible")

    structure["_contract"] = default_contract()
    return structure
