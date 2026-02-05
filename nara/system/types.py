from enum import Enum

class SystemType(str, Enum):
    EXECUTABLE = "executable"
    ANALYSIS = "analysis"
    HYBRID = "hybrid"
