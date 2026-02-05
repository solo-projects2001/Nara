# nara/tests/regression_runner.py
"""
Enterprise Regression Runner

Runs golden intents and checks deterministic domain resolution.
"""

import json
from nara.core.intent import parse_intent, infer_structure


def run_regression():
    with open("nara/tests/golden_intents.json", "r") as f:
        cases = json.load(f)

    ok = True

    for case in cases:
        intent = case["intent"]
        expected = case["expected_domain"]

        structure = infer_structure(parse_intent(intent))
        got = structure["_domain"]["domain"]

        if got != expected:
            print("FAIL:", intent)
            print(" expected:", expected)
            print(" got:", got)
            ok = False
        else:
            print("PASS:", intent)

    return ok


if __name__ == "__main__":
    success = run_regression()
    raise SystemExit(0 if success else 1)
