from nara.domains.analysis.default import DefaultAnalysisAnalyzer
from nara.domains.analysis.interpreted import InterpretedAnalyzer
from nara.domains.analysis.compiled import CompiledAnalyzer
from nara.domains.analysis.shell import ShellAnalyzer
from nara.domains.analysis.data import DataAnalyzer


ANALYZERS = {
    # Top-level analysis handler (must implement .run)
    "analysis": DefaultAnalysisAnalyzer(),

    # Subdomain analyzers (optional specialized)
    "interpreted": InterpretedAnalyzer(),
    "compiled": CompiledAnalyzer(),
    "shell": ShellAnalyzer(),
    "data": DataAnalyzer(),
}


def get_analyzer(domain_name: str):
    domain = domain_name.strip().lower()

    if domain not in ANALYZERS:
        raise RuntimeError(f"no_analyzer_for_domain: {domain}")

    return ANALYZERS[domain]
