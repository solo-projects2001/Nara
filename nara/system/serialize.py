def serialize_system_declaration(decl) -> dict:
    return {
        "system_type": decl.system_type.value,
        "reason": decl.reason
    }
