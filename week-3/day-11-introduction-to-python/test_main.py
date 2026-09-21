"""
Day 11 — Submission checklist.
Checks that all required files are present and the script has no syntax errors.
"""

import subprocess
import sys
from pathlib import Path

SCRIPT = Path("week-3/day-11-introduction-to-python/main.py")


def test_main_py_exists():
    """main.py must be submitted."""
    assert SCRIPT.exists(), (
        "main.py not found. Make sure you saved the file in "
        "week-3/day-11-introduction-to-python/main.py"
    )


def test_main_py_not_empty():
    """main.py must contain code — not just the starter comments."""
    content = SCRIPT.read_text().strip()
    lines = [l for l in content.splitlines() if l.strip() and not l.strip().startswith("#")]
    assert len(lines) >= 5, (
        f"main.py appears to be mostly empty ({len(lines)} non-comment lines). "
        "Complete all three exercises before submitting."
    )


def test_no_syntax_errors():
    """main.py must have no syntax errors."""
    result = subprocess.run(
        [sys.executable, "-m", "py_compile", str(SCRIPT)],
        capture_output=True, text=True
    )
    assert result.returncode == 0, (
        f"Syntax error found in main.py:\n{result.stderr}"
    )
