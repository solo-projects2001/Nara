from dataclasses import dataclass

@dataclass
class SystemInterface:
    inputs: list[str]
    outputs: list[str]

    def compatible_with(self, other: "SystemInterface") -> bool:
        return all(o in other.inputs for o in self.outputs)
