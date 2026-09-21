"""
Day 15 — Submission checklist.
Checks that the complete project is present: script, data folder, and filled-in README.
"""

import subprocess
import sys
from pathlib import Path

SCRIPT = Path("week-3/day-15-automation-project/main.py")
README = Path("week-3/day-15-automation-project/README.md")
DATA_DIR = Path("week-3/day-15-automation-project/data")

UNFILLED_PLACEHOLDERS = [
    "<!-- Describe your project",
    "<!-- State which option",
    "<!-- List any Python",
    "<!-- Paste or screenshot",
]


def test_main_py_exists():
    """main.py must be submitted."""
    assert SCRIPT.exists(), (
        "main.py not found. Save it in week-3/day-15-automation-project/main.py"
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
        "Build your full automation project before submitting."
    )


def test_readme_exists():
    """README.md must be present."""
    assert README.exists(), (
        "README.md is missing. "
        "Every Day 15 submission requires a README explaining the project."
    )


def test_readme_placeholders_removed():
    """README.md must have all template placeholders replaced with real content."""
    content = README.read_text()
    remaining = [p for p in UNFILLED_PLACEHOLDERS if p in content]
    assert len(remaining) == 0, (
        f"README.md still has {len(remaining)} unfilled section(s):\n"
        + "\n".join(f"  - {p}" for p in remaining)
        + "\nReplace every HTML comment placeholder with your own content."
    )


def test_readme_has_content():
    """README.md must have meaningful content (at least 100 characters beyond the title)."""
    content = README.read_text().strip()
    assert len(content) >= 100, (
        f"README.md is too short ({len(content)} chars). "
        "Add a proper description, requirements, and how-to-run section."
    )


def test_data_folder_exists():
    """data/ folder must be present for input and output files."""
    assert DATA_DIR.is_dir(), (
        "data/ folder is missing. "
        "Create it and place any input files your script needs inside it."
    )
