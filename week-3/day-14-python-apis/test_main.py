"""
Day 14 — Submission checklist.
Checks that all required files are present and no secrets were committed.
"""

import subprocess
import sys
from pathlib import Path

SCRIPT = Path("week-3/day-14-python-apis/main.py")
ENV_EXAMPLE = Path("week-3/day-14-python-apis/.env.example")
ENV_FILE = Path("week-3/day-14-python-apis/.env")


def test_main_py_exists():
    """main.py must be submitted."""
    assert SCRIPT.exists(), (
        "main.py not found. Save it in week-3/day-14-python-apis/main.py"
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
        "Implement fetch_data and display_results before submitting."
    )


def test_env_example_committed():
    """.env.example must be committed so reviewers know which keys are needed."""
    assert ENV_EXAMPLE.exists(), (
        ".env.example is missing. "
        "Copy your .env format (with placeholder values, not real keys) "
        "and commit it as .env.example"
    )


def test_env_file_not_committed():
    """.env must NOT be committed — it contains your real API key."""
    assert not ENV_FILE.exists(), (
        ".env was committed to the repository. "
        "This exposes your API key publicly. Remove it immediately:\n"
        "  git rm --cached week-3/day-14-python-apis/.env\n"
        "  git commit -m 'fix: remove committed .env file'\n"
        "Then add .env to your .gitignore."
    )


def test_requests_imported():
    """main.py must import the requests library."""
    content = SCRIPT.read_text()
    assert "import requests" in content, (
        "requests is not imported in main.py. "
        "Add 'import requests' at the top of the file."
    )
