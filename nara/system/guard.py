from nara.system.types import SystemType

def validate_system_type(system_type: SystemType, domain: str):
    if system_type == SystemType.ANALYSIS and domain not in ["analysis"]:
        raise RuntimeError("analysis_system_with_execution_domain")

    if system_type == SystemType.EXECUTABLE and domain == "analysis":
        raise RuntimeError("executable_system_with_analysis_domain")
