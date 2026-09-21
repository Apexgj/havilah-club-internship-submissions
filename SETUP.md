# Setup and Git Guide

Everything you need to get started: installing the tools, setting up your fork, working on tasks, and opening a PR to submit your work.

---

## 1. Install the Required Tools

Do this once before anything else.

### Python 3

Download and install from [python.org/downloads](https://python.org/downloads/).

Confirm it worked:
```bash
python --version
```
You should see `Python 3.x.x`. If the command is not found or shows `Python 2.x.x`, try `python3 --version` and use `python3` in place of `python` throughout this guide.

### Git

Download and install from [git-scm.com/downloads](https://git-scm.com/downloads).

Confirm it worked:
```bash
git --version
```

### VS Code

Download from [code.visualstudio.com](https://code.visualstudio.com/). After installing, open the Extensions panel (Ctrl+Shift+X on Windows/Linux, Cmd+Shift+X on Mac) and install the **Python** extension.

---

## 2. Configure Git with Your Identity

Run these two commands once after installing Git. Use your real name and the email address linked to your GitHub account.

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your@email.com"
```

Verify the configuration was saved:
```bash
git config --global --list
```

---

## 3. Fork the Repository

You do not clone the original repository directly. You create your own copy (a fork) first.

1. Open [github.com/Havilah-Blockchain-Studios/havilah-club-internship-submissions](https://github.com/Havilah-Blockchain-Studios/havilah-club-internship-submissions) in your browser.
2. Click the **Fork** button in the top-right corner of the page.
3. Under "Owner", select your personal GitHub account from the dropdown.
4. Leave the repository name as is and click **Create fork**.

Your fork will be created at `https://github.com/your-username/havilah-club-internship-submissions`. This is your personal working copy — you push all your work here.

---

## 4. Clone Your Fork

Clone **your fork**, not the original. Replace `your-username` with your actual GitHub username.

```bash
git clone https://github.com/your-username/havilah-club-internship-submissions.git
cd havilah-club-internship-submissions
```

You only need to do this once. From now on, open the terminal inside the `havilah-club-internship-submissions` folder when working on tasks.

---

## 5. Fill In Your Student Profile

Before working on any task, open `STUDENT.md` and fill in every field — your full name, GitHub username, email, cohort, and learning objective.

Save the file, then commit and push it:

```bash
git add STUDENT.md
git commit -m "feat: add student profile"
git push
```

This is the first thing instructors look at when they open your PR. Do not skip it.

---

## 6. Daily Task Workflow

Repeat these steps each day for the current task.

### Step 1 — Check your status

Always start by checking what state your repository is in:

```bash
git status
```

This shows which files have been changed, staged, or are untracked.

### Step 2 — Open the day's folder in VS Code

```bash
code week-3/day-11-introduction-to-python
```

Replace `day-11-introduction-to-python` with the correct folder for the day you are working on.

### Step 3 — Complete the task

Open `main.py` and implement the code for each TODO section. Run your script regularly to test it:

```bash
python week-3/day-11-introduction-to-python/main.py
```

Do not edit `test_main.py` or `test_submission.py` — those files are used by the automated checks.

### Step 4 — Stage your files

When your work is ready to commit, stage the specific files you changed:

```bash
git add week-3/day-11-introduction-to-python/main.py
```

To stage everything inside a day folder at once:

```bash
git add week-3/day-11-introduction-to-python/
```

**Do not use `git add .`** — it can accidentally include your `.env` file, which contains your API key.

### Step 5 — Commit with a clear message

A commit is a permanent snapshot of your work. Write a short, meaningful message:

```bash
git commit -m "feat(day-11): complete introduction to Python exercises"
```

Commit message format:

```
feat(day-XX): short description of what you completed
fix(day-XX): short description of what you corrected
```

### Step 6 — Push to your fork

```bash
git push
```

This uploads your commit to your fork on GitHub. The automated checks will run on your fork and you can see the results under the **Actions** tab.

---

## 7. Day 13 — Committing the Output CSV

Your script generates `data/output.csv` when it runs. You must commit this file as part of your Day 13 submission.

Run your script first:
```bash
python week-3/day-13-working-with-data/main.py
```

Then add and commit the output file:
```bash
git add week-3/day-13-working-with-data/data/output.csv
git commit -m "feat(day-13): add generated output CSV"
git push
```

---

## 8. Day 14 — API Keys and Environment Files

Your API key is a secret. Never put it directly in your code or commit it to GitHub.

**Setting up your `.env` file:**

Create a file named `.env` inside `week-3/day-14-python-apis/`:
```
API_KEY=your_real_api_key_here
```

This file stays on your computer only. The `.gitignore` already prevents it from being committed.

**Reading the key in your Python script:**
```python
import os
API_KEY = os.getenv("API_KEY", "")
```

**Committing `.env.example` instead:**

The `.env.example` file already exists with a placeholder value. Commit it so reviewers know which keys are needed — but never put real values in it:
```bash
git add week-3/day-14-python-apis/.env.example
git commit -m "feat(day-14): add env example"
git push
```

**Confirm `.env` is not being tracked:**
```bash
git status
```
Your `.env` file must not appear in this list. If it does, do not stage it.

---

## 9. Opening Your Pull Request

Once all tasks for the week are done and pushed, open a Pull Request to submit your work.

1. Go to your fork on GitHub: `https://github.com/your-username/havilah-club-internship-submissions`
2. You will see a banner saying your branch is ahead of the original — click **Contribute**, then **Open pull request**.
3. On the PR creation page, confirm:
   - **Base repository:** `Havilah-Blockchain-Studios/havilah-club-internship-submissions`
   - **Base branch:** `main`
   - **Head repository:** `your-username/havilah-club-internship-submissions`
   - **Compare branch:** `main`
4. The PR description will be pre-filled with a template. Fill in **every section**:
   - Your full name and GitHub username in the Student Details table
   - The cohort number and week number
   - Tick each task you completed in the checklist
   - Paste your social media post link for each day in the table
   - Add any notes for your instructor in the Notes section
5. Set the PR title to: `[Week 3] Your Full Name — Week 3 Submissions`
6. Click **Create pull request**.

After opening the PR, GitHub will run the automated submission checks. You will see the results in the **Checks** section at the bottom of the PR. All checks must be green before your PR is reviewed.

---

## 10. Fixing a Failed Check

If a check fails after you open your PR:

1. Click the failing check to read the exact error message.
2. Fix the issue in your local copy.
3. Commit and push the fix to your fork:
   ```bash
   git add <file>
   git commit -m "fix(day-XX): resolve missing output CSV"
   git push
   ```
4. The checks on your open PR will re-run automatically. You do not need to open a new PR.

---

## 11. Keeping Your Fork Up to Date

If the original repository is updated after you forked it (for example, new weeks are added), sync your fork to get the latest files:

```bash
git remote add upstream https://github.com/Havilah-Blockchain-Studios/havilah-club-internship-submissions.git
git fetch upstream
git merge upstream/main
git push
```

You only need to add the `upstream` remote once. After that, just run `git fetch upstream`, `git merge upstream/main`, and `git push`.

---

## 12. Common Errors and Fixes

**"fatal: not a git repository"**
You are not inside the project folder. Run:
```bash
cd havilah-club-internship-submissions
```

**"Permission denied (publickey)"**
Switch to HTTPS authentication:
```bash
git remote set-url origin https://github.com/your-username/havilah-club-internship-submissions.git
```

**"Your branch is behind 'origin/main'"**
Your local copy is out of date with your fork. Pull the latest changes first:
```bash
git pull
```
Then push your work.

**"Updates were rejected because the remote contains work you do not have locally"**
Same as above — pull first, then push:
```bash
git pull --rebase
git push
```

**Accidentally staged `.env`**
Remove it from staging without deleting the file:
```bash
git rm --cached week-3/day-14-python-apis/.env
git commit -m "fix: remove .env from git tracking"
git push
```

**Syntax error in your Python script**
Find the exact line causing the error:
```bash
python -m py_compile week-3/day-11-introduction-to-python/main.py
```

**PR checks are failing but your script runs fine locally**
Make sure you committed and pushed the latest version of your file. Run `git status` — if it shows modified files, you have unsaved commits.
