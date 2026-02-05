# nara/core/dag/schema.py
from dataclasses import dataclass

@dataclass
class DAGNode:
    id: str
    entrypoint: str
    depends_on: list[str]
