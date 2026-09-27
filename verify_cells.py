import re
import sys
import glob
import traceback

import matplotlib
matplotlib.use("Agg")

CELL_RE = re.compile(r"```\{pyodide\}\n(.*?)```", re.DOTALL)
OPT_RE = re.compile(r"^\s*#\|.*$", re.MULTILINE)

failures = 0
files = sorted(glob.glob("part-*/*.qmd")) + ["index.qmd"]
report = []

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
            tb = traceback.extract_tb(sys.exc_info()[2])
            last = tb[-1]
            line = (last.line or "").strip()[:90]
            report.append(f"{path} | cell {i} | {sys.exc_info()[0].__name__}: "
                          f"{sys.exc_info()[1]} | at: {line}")

for r in report:
    print(r)
print(f"\nDone. {failures} failing cells across {len(files)} files.")
sys.exit(1 if failures else 0)
