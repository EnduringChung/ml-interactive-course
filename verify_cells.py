import re
import sys
import glob
import traceback

import matplotlib
matplotlib.use("Agg")

CELL_RE = re.compile(r"```\{pyodide\}\n(.*?)```", re.DOTALL)
OPT_RE = re.compile(r"^\s*#\|\s*\w+:.*$", re.MULTILINE)

failures = 0
files = sorted(glob.glob("part-*/*.qmd")) + ["index.qmd"]

for path in files:
    text = open(path, encoding="utf-8").read()
    cells = CELL_RE.findall(text)
    ns = {}
    for i, code in enumerate(cells, 1):
        cleaned = OPT_RE.sub("", code)
        try:
            exec(compile(cleaned, f"{path}:cell{i}", "exec"), ns)
        except Exception:
            failures += 1
            print(f"\n=== FAIL {path} cell {i} ===")
            traceback.print_exc(limit=3)
            print("--- code was ---")
            print(cleaned)

print(f"\nDone. {failures} failing cells across {len(files)} files.")
sys.exit(1 if failures else 0)
