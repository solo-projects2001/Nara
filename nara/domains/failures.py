DOMAIN_FAILURES = {
    "interpreted": {
        "syntax_error",
        "runtime_error",
        "module_not_found",
        "contract_violation",
    },
    "compiled": {
        "compile_error",
        "link_error",
        "binary_missing",
        "runtime_error",
    },
    "shell": {
        "command_not_found",
        "permission_denied",
        "nonzero_exit",
    },
    "data": {
        "query_error",
        "schema_mismatch",
        "empty_result",
    },
}
