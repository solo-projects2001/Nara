from dataclasses import dataclass
from typing import Callable, Any

@dataclass
class Precondition:
    check: Callable[[dict], bool]
    description: str

@dataclass
class Postcondition:
    check: Callable[[dict], bool]
    description: str

@dataclass
class Invariant:
    check: Callable[[dict], bool]
    description: str

@dataclass
class Contract:
    preconditions: list[Precondition]
    postconditions: list[Postcondition]
    invariants: list[Invariant]
