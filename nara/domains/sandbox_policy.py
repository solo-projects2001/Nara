class SandboxPolicy:
    def __init__(self, fs_read=True, fs_write=True, network=False, tools=None):
        self.fs_read = fs_read
        self.fs_write = fs_write
        self.network = network
        self.tools = tools or []
