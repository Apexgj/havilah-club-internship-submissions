# Setup and Git Guide

Everything you need to get started, submit your work, and understand the automated checks.

---

## 1. Prerequisites

Install these before anything else.

### Python 3

Download from [python.org](https://python.org/downloads/) and install.

Verify it worked:
```bash
python --version
```
You should see `Python 3.x.x`. If you see `Python 2.x.x`, use `python3` instead of `python` in all commands below.

### Git

Download from [git-scm.com](https://git-scm.com/downloads) and install.

Verify:
```bash
git --version
```

### VS Code

Download from [code.visualstudio.com](https://code.visualstudio.com/). Install the **Python** extension from the Extensions panel (Ctrl+Shift+X).

---

## 2. One-time Git Setup

Run these once after installing Git. Replace the values with your own name and email.

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your@email.com"
```

---

## 3. Clone This Repository

This is how you get the starter files onto your computer.

```bash
git clone https://github.com/kingfavourjudah/havilah-club-internship-submissions.git
cd havilah-club-internship-submissions
```

You only need to do this once.

---

## 4. Daily Workflow

Follow these steps every day when working on a task.

### Step 1 — Check your current status
```bash
git status
```
This shows which files have been changed or added.

### Step 2 — Open the day's folder in VS Code
```bash
code week-3/day-11-introduction-to-python
```

### Step 3 — Work on your task

Complete all the TODOs in `main.py`. Run your script to test it:
```bash
python week-3/day-11-introduction-to-python/main.py
```

### Step 4 — Stage your changes

When you are ready to submit, stage the files you changed:
```bash
git add week-3/day-11-introduction-to-python/main.py
```

To stage everything in a day's folder:
```bash
git add week-3/day-11-introduction-to-python/
```

**Do not use `git add .` until you have read about .gitignore — you may accidentally add your .env file.**

### Step 5 — Commit your changes

A commit is a saved snapshot of your work. Write a short message describing what you did:
```bash
git commit -m "feat(day-11): complete introduction to Python exercises"
```

Commit message format:
```
feat(day-XX): short description of what you did
fix(day-XX): short description of what you fixed
```

### Step 6 — Push to GitHub
```bash
git push
```

This uploads your commit to GitHub, where the automated checks will run.

---

## 5. Day 13 — Submitting CSV Files

After running your script, an `output.csv` file will be created in the `data/` folder.
You must add this file to your commit:

```bash
git add week-3/day-13-working-with-data/data/output.csv
git commit -m "feat(day-13): add generated output CSV"
git push
```

---

## 6. Day 14 — API Keys and .env Files

**Never commit your API key.** Follow these steps:

1. Create a `.env` file in `week-3/day-14-python-apis/` (this file stays on your computer only):
   ```
   API_KEY=your_real_key_here
   ```

2. In your Python script, read it like this:
   ```python
   import os
   API_KEY = os.getenv("API_KEY", "")
   ```

3. The `.gitignore` file already prevents `.env` from being pushed. Confirm:
   ```bash
   git status
   ```
   Your `.env` file should NOT appear in the list. If it does, do not stage it.

---

## 7. Understanding the Automated Checks

Every time you push to GitHub, automated checks run on your submission. You can see the results under the **Actions** tab on GitHub.

- **Green checkmark** — your submission passes all checks for that day.
- **Red X** — something is missing or has an error. Click the failed job to read the error message.

The checks verify:
- Your required files are present
- Your script has no syntax errors
- Required deliverables (CSVs, READMEs) have been committed

The checks do **not** grade the quality of your work — your instructor does that.

---

## 8. Common Problems and Fixes

**"fatal: not a git repository"**
You are not inside the cloned folder. Run `cd havilah-club-internship-submissions` first.

**"Permission denied (publickey)"**
You need to set up SSH keys or use HTTPS. Run:
```bash
git remote set-url origin https://github.com/kingfavourjudah/havilah-club-internship-submissions.git
```

**"Your branch is behind 'origin/main'"**
Someone else pushed changes. Pull them first:
```bash
git pull
```
Then push your work.

**Accidentally staged .env**
```bash
git rm --cached week-3/day-14-python-apis/.env
git commit -m "fix: remove .env from tracking"
git push
```

**Syntax error in your Python script**
Run this to see the exact line with the error:
```bash
python -m py_compile week-3/day-11-introduction-to-python/main.py
```
