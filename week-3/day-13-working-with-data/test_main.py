"""
Day 13 — Submission checklist.
Checks that the script, original CSV, and output CSV are all submitted.
"""

import subprocess
import sys
from pathlib import Path

SCRIPT = Path("week-3/day-13-working-with-data/main.py")
SAMPLE_CSV = Path("week-3/day-13-working-with-data/data/sample.csv")
OUTPUT_CSV = Path("week-3/day-13-working-with-data/data/output.csv")


def test_main_py_exists():
    """main.py must be submitted."""
    assert SCRIPT.exists(), (
        "main.py not found. Save it in week-3/day-13-working-with-data/main.py"
    )


def test_no_syntax_errors():
    """main.py must have no syntax errors."""
    result = subprocess.run(
        [sys.executable, "-m", "py_compile", str(SCRIPT)],
        capture_output=True, text=True
    )
    assert result.returncode == 0, f"Syntax error in main.py:\n{result.stderr}"


def test_main_py_not_empty():
    """main.py must contain implemented code."""
    content = SCRIPT.read_text()
    lines = [l for l in content.splitlines() if l.strip() and not l.strip().startswith("#")]
    assert len(lines) >= 10, (
        f"main.py appears to be mostly empty ({len(lines)} non-comment lines). "
        "Implement all four steps: load, summarise, filter, and export."
    )


def test_sample_csv_present():
    """data/sample.csv must be present — do not delete it."""
    assert SAMPLE_CSV.exists(), (
        "data/sample.csv is missing. "
        "Include the original dataset you used in your submission."
    )


def test_output_csv_present():
    """data/output.csv must be committed — run your script locally first."""
    assert OUTPUT_CSV.exists(), (
        "data/output.csv is missing. "
        "Run your script locally (python main.py) to generate the output file, "
        "then add it to your commit: git add week-3/day-13-working-with-data/data/output.csv"
    )


def test_output_csv_not_empty():
    """data/output.csv must contain data."""
    content = OUTPUT_CSV.read_text().strip()
    assert len(content) > 0, (
        "data/output.csv is empty. "
        "Run your script with the sample data and commit the generated output."
    )
