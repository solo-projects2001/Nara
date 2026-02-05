# nara/ux/governance/roles.py
from enum import Enum

class Role(str, Enum):
    VIEWER = "viewer"
    OPERATOR = "operator"
    AUDITOR = "auditor"
    ADMIN = "admin"
