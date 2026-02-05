def confidence(successes: int, failures: int) -> float:
    total = successes + failures
    return 1.0 if total == 0 else successes / total
