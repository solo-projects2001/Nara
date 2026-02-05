from dataclasses import dataclass
from nara.system.types import SystemType

@dataclass
class SystemDeclaration:
    system_type: SystemType
    reason: str
