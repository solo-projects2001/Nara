def score(candidate: str, original: str) -> int:
    diff_size = abs(len(candidate) - len(original))
    return diff_size
