import os
import json


class SimpleAnalysisAnalyzer:
    """
    Enterprise-safe analysis runtime:
    - No execution
    - Only produces an inspectable report artifact
    """

    def run(self, artifacts: dict):
        root = artifacts["root"]
        report_path = os.path.join(root, "analysis_report.json")

        report = {
            "status": "analysis_complete",
            "artifacts": list(artifacts["files"].keys()),
            "note": "No execution performed. Inspection-only domain.",
        }

        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)

        return {
            "ok": True,
            "report": report_path,
        }
