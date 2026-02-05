from nara.domains.sandbox_policy import SandboxPolicy

POLICIES = {
    "interpreted": SandboxPolicy(
        fs_read=True,
        fs_write=True,
        network=False,
        tools=["python", "node", "ruby", "lua"]
    ),
    "compiled": SandboxPolicy(
        fs_read=True,
        fs_write=True,
        network=False,
        tools=["gcc", "clang", "rustc", "go"]
    ),
    "shell": SandboxPolicy(
        fs_read=True,
        fs_write=True,
        network=False,
        tools=["bash", "pwsh", "cmd"]
    ),
    "data": SandboxPolicy(
        fs_read=True,
        fs_write=False,
        network=False,
        tools=["sqlite3", "duckdb"]
    ),
}
