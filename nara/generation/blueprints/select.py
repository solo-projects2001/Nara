# nara/generation/blueprints/select.py
from nara.generation.blueprints.types import BlueprintType

def select_blueprint(intent: str) -> BlueprintType:
    low = intent.lower()

    if "csv" in low or "pipeline" in low:
        return BlueprintType.ETL_PIPELINE

    if "compliance" in low or "inspect" in low:
        return BlueprintType.COMPLIANCE_SCANNER

    if "log" in low or "monitor" in low:
        return BlueprintType.LOG_MONITORING

    if "benchmark" in low or "evaluate" in low:
        return BlueprintType.BENCHMARK_RUNNER

    if "tool" in low or "harness" in low:
        return BlueprintType.TOOL_HARNESS

    if "report" in low:
        return BlueprintType.REPORT_SYSTEM

    return BlueprintType.DEFAULT
