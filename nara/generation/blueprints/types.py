# nara/generation/blueprints/types.py
from enum import Enum

class BlueprintType(str, Enum):
    ETL_PIPELINE = "etl_pipeline"
    COMPLIANCE_SCANNER = "compliance_scanner"
    LOG_MONITORING = "log_monitoring"
    TOOL_HARNESS = "tool_harness"
    BENCHMARK_RUNNER = "benchmark_runner"
    REPORT_SYSTEM = "report_system"
    DEFAULT = "default"
