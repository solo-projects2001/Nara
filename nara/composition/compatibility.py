from nara.composition.interfaces import SystemInterface

def check_compatibility(interfaces: list[SystemInterface]) -> bool:
    for i in range(len(interfaces) - 1):
        if not interfaces[i].compatible_with(interfaces[i + 1]):
            return False
    return True
