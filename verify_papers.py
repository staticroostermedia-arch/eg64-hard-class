#!/usr/bin/env python3
"""Run all seed suites cited by Papers I and II."""
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parent
scripts = [
    "verify_gaps.py",
    "verify_universal.py",
    "verify_purenew.py",
    "verify_freeport.py",
    "verify_open201.py",
    "verify_open_remaining.py",
    "verify_rigorous.py",
    "verify_closed.py",
]
failed = []
for s in scripts:
    print(f"=== {s} ===")
    r = subprocess.run([sys.executable, str(root / s)], capture_output=True, text=True)
    print(r.stdout[-800:] if r.stdout else "")
    if r.returncode != 0:
        print(r.stderr[-500:])
        failed.append(s)
if failed:
    print("FAILED:", failed)
    sys.exit(1)
print("ALL paper verification suites PASS")
