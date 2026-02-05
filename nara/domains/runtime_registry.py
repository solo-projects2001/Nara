from nara.domains.interpreted_runtime import InterpretedRuntime
from nara.domains.compiled_runtime import CompiledRuntime
from nara.domains.shell_runtime import ShellRuntime
from nara.domains.analysis_runtime import AnalysisRuntime

RUNTIMES = {
    "interpreted": InterpretedRuntime(),
    "compiled": CompiledRuntime(),
    "shell": ShellRuntime(),
    "data": InterpretedRuntime(),
    "analysis": AnalysisRuntime(),
}


def get_runtime(domain_name: str):
    if domain_name not in RUNTIMES:
        raise RuntimeError(f"no_runtime_for_domain: {domain_name}")
    return RUNTIMES[domain_name]
