from nara.system.types import SystemType
from nara.system.declaration import SystemDeclaration


def resolve_system_type(intent: str) -> SystemDeclaration:
    """
    Enterprise Correct System Typing

    ANALYSIS   = inspection-only (no execution)
    EXECUTABLE = pipelines, ETL, processing, generation
    HYBRID     = analyze then execute

    Fix:
    - Validation/reporting inside pipelines is still EXECUTABLE
    """

    low = intent.lower()

    # True inspection-only analysis keywords
    analysis_only_keys = [
        "inspect",
        "audit",
        "scan",
        "compliance",
        "inventory",
        "risk classification",
    ]

    # Executable pipeline keywords
    executable_keys = [
        "pipeline",
        "etl",
        "load",
        "ingest",
        "process",
        "aggregate",
        "validate csv",
        "write report",
        "export",
        "generate",
        "monitor",
        "metrics",
    ]

    has_analysis_only = any(k in low for k in analysis_only_keys)
    has_exec = any(k in low for k in executable_keys)

    # HYBRID only when explicit inspection + execution appear together
    if has_analysis_only and has_exec:
        return SystemDeclaration(
            system_type=SystemType.HYBRID,
            reason="inspection_plus_execution_detected",
        )

    # Pure inspection systems
    if has_analysis_only:
        return SystemDeclaration(
            system_type=SystemType.ANALYSIS,
            reason="inspection_only_detected",
        )

    # Everything else defaults to executable
    return SystemDeclaration(
        system_type=SystemType.EXECUTABLE,
        reason="default_pipeline_execution",
    )
