from dataclasses import dataclass

@dataclass
class GraphNode:
    name: str
    role: str

@dataclass
class GraphEdge:
    source: str
    target: str
    label: str
