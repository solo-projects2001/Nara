# scripts/run_tests.ps1
python -m pytest
python nara/tests/regression_runner.py
