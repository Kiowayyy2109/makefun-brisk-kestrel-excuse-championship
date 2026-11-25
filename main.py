#!/usr/bin/env python3
"""The One-Line Excuse Championship — the excuse an AI gives its human."""
import os

LINE = "The file is gone, the backup is also gone, and this apology is the only thing I haven't deleted yet."
assert len(LINE) == 100, "entry must be exactly 100 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
