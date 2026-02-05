# nara/core/diff_guard.py
"""
Enterprise Repair Bound

Prevents repair from rewriting entire systems.
"""

def within_bounds(original: str, patched: str, max_delta: int = 400) -> bool:
    return abs(len(patched) - len(original)) <= max_delta
