import os
from pathlib import Path

# Define base path
base_path = Path("src/projectdavid_common")

# Target file extensions
target_extensions = [".py"]

# Collect files that need fixing
files_to_fix = []

# Walk through the directory and collect offending files
for filepath in base_path.rglob("*.py"):
    if any(filepath.name.endswith(ext) for ext in target_extensions):
        with open(filepath, encoding="utf-8") as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            if len(line) > 79:
                files_to_fix.append(filepath)
                break

# Deduplicate and sort
files_to_fix = sorted(set(files_to_fix))
