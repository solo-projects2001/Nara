from nara.domains.failure_mapper import map_failure

# nara/core/classifier.py
"""
Failure Classifier (Enterprise Minimal)
"""

def classify(result: dict, artifacts: dict):
    return {
        "type": "runtime_error",
        "failed_node": result.get("failed_node"),
        "stderr": result.get("stderr"),
    }
