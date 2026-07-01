# Daily LeetCode

Personal LeetCode practice repo for learning:
- Python
- TypeScript
- JavaScript
- Go
- Debugging
- Data structures & algorithms

---

# Project Structure

daily-leetcode/  
├── .venv/                 Python virtual environment  
├── pyproject.toml         Ruff/Python tooling config  
├── requirements.txt  
├── README.md  

├── easy/  
│   ├── merge_two_sorted_array.py  
│   └── .vscode/  
│       └── settings.json  

├── twosum.py  
├── twosum.js  
├── twosum.ts  
└── twosum.go  

---

# Python Setup

Create virtual environment:

    python3 -m venv .venv

Activate virtual environment on macOS/Linux:

    source .venv/bin/activate

Activate virtual environment on Windows:

    .venv\Scripts\activate

---

# Install Dependencies

Install Ruff:

    python -m pip install ruff

Save dependencies:

    pip freeze > requirements.txt

Install from requirements later:

    pip install -r requirements.txt

---

# Running Python Problems

Run a file:

    python easy/merge_two_sorted_array.py

or:

    python3 easy/merge_two_sorted_array.py

---

# Example Local Test

Example test data:

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    Solution().merge(nums1, m, nums2, n)

    print(nums1)

Expected output:

    [1, 2, 2, 3, 5, 6]

---

# VS Code Debugging

Start debugger:

1. Open Python file  
2. Click left gutter to create breakpoint  
3. Press F5  
4. Select “Python File”

---

# Useful VS Code Shortcuts

Problems panel:

    Cmd + Shift + M

Quick Fix:

    Cmd + .

Command Palette:

    Cmd + Shift + P

---

# Ruff Formatting & Linting

Format files:

    ruff format .

Check lint errors:

    ruff check .

Auto-fix issues:

    ruff check . --fix

---

# Learning Goals

- Understand time complexity
- Learn debugging workflows
- Improve algorithm intuition
- Become comfortable reading error messages
- Build consistency through daily practice