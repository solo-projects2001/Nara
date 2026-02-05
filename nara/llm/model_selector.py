def choose(task: str) -> str:
    if "repair" in task:
        return "deepseek-coder:6.7b"
    return "qwen2.5:14b"
