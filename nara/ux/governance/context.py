# nara/ux/governance/context.py
from nara.ux.governance.roles import Role

class UXContext:
    def __init__(self, role: Role):
        self.role = role

    def can_run(self):
        return self.role in (Role.OPERATOR, Role.ADMIN)

    def can_view_audit(self):
        return self.role in (Role.AUDITOR, Role.ADMIN)

    def can_override(self):
        return self.role == Role.ADMIN
