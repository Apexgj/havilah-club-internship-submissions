# Day 15 — Python Automation Project
# Choose one project type and implement it here:
#
#   A) File Organiser  — scans a folder and moves files into subfolders by extension
#   B) Report Generator — reads a CSV and produces a formatted text summary
#   C) Data Cleaner    — removes duplicate rows, strips whitespace, standardises columns
#
# Submit the complete project (this file + data folder + README.md) to GitHub.

import os
# import shutil   # uncomment if using File Organiser
# import csv      # uncomment if using Report Generator or Data Cleaner


# ── Configuration ─────────────────────────────────────────────────────────────
# Set your input/output paths here so they are easy to find and change.

INPUT_PATH = "data/"
OUTPUT_PATH = "data/output/"


# ── Core Functions ─────────────────────────────────────────────────────────────
# Break your project into small, clearly named functions.
# Each function should do one thing.

def process(input_path, output_path):
    # TODO: implement your chosen project logic here
    pass


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("Starting automation...")
    process(INPUT_PATH, OUTPUT_PATH)
    print("Done.")


if __name__ == "__main__":
    main()
