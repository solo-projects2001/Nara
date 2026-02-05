# nara/generation/blueprints/registry.py
from nara.generation.blueprints.types import BlueprintType

BLUEPRINTS = {
    BlueprintType.ETL_PIPELINE: {
        "roles": ["ingestor", "validator", "aggregator", "reporter"]
    },
    BlueprintType.COMPLIANCE_SCANNER: {
        "roles": ["scanner", "rule_engine", "findings_export"]
    },
    BlueprintType.LOG_MONITORING: {
        "roles": ["tailer", "parser", "metrics", "alert_report"]
    },
    BlueprintType.TOOL_HARNESS: {
        "roles": ["adapter", "runner", "collector"]
    },
    BlueprintType.BENCHMARK_RUNNER: {
        "roles": ["suite_loader", "executor", "scoreboard"]
    },
    BlueprintType.REPORT_SYSTEM: {
        "roles": ["loader", "formatter", "exporter"]
    },
    BlueprintType.DEFAULT: {
        "roles": ["loader", "processor", "reporter"]
    },
}
