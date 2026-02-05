def generate_requirements(domain: str) -> str:
    if domain == "interpreted":
        return "python>=3.10\n"
    return ""
