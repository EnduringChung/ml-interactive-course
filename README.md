# ML, Statistics & LLM — Interactive Course

An interactive machine-learning, statistics, and LLM course (with a biological-data thread), built with [Quarto Live](https://github.com/r-wasm/quarto-live) and hosted on **GitHub Pages**. All code cells run **in the browser** (Pyodide/webR) — designed first for reading in **Safari on iPad**.

**Live site:** https://enduringchung.github.io/ml-interactive-course/

## Structure

```
_quarto.yml                    site config (format: live-html, engine: markdown)
index.qmd                      course home: how-to, tier legend, course map
part-00-python-foundations/    00-1 … 00-5   (T1)
part-01-statistics-bridge/     01-1 … 01-5   (T1)
part-02…part-13, appendix-a/   placeholder stubs until built (build order in plan.md)
_extensions/r-wasm/live/       quarto-live extension (vendored via `quarto add`)
assets/                        styles
```

Every subtopic page follows the same seven-section template: Basic Concept → Concept Questions → Drills & Exercises → Advanced Information & Pitfalls (incl. "Read & Refactor AI Code") → Advanced Questions → Complex Questions → Summary.

Tiers: **T1** live cells (run here), **T2** frozen output + local script, **T3** Colab/local badge.

## Local development

Quarto runs in the `ml-course` conda environment (from conda-forge; the launcher needs
`QUARTO_SHARE_PATH` set when invoked without activation):

```bash
conda activate ml-course
quarto render          # builds the site into _site/
quarto preview         # live-reload preview server
```

To publish: `quarto publish gh-pages` (pushes the `gh-pages` branch; Pages serves it).

## Editing content

- Pages are `.qmd` with `format: live-html` inherited from `_quarto.yml`; declare `tier:` in frontmatter.
- Declare page dependencies under frontmatter `pyodide: packages:` (installed in-browser at load).
- Always end plotting cells with `plt.show()`; set `#| fig-width` / `#| fig-height` cell options.
- Before publishing, run the cell-extraction smoke test (executes every `{pyodide}` cell):

  ```bash
  python verify_cells.py   # (kept out of the site; see repo tooling note below)
  ```

## Page status tracker

Status flow: **Draft → Drilled → Reviewed → Published**

| Page | Tier | Status |
|---|---|---|
| 0.1 Python for numerical work | T1 | Published |
| 0.2 NumPy | T1 | Published |
| 0.3 pandas | T1 | Published |
| 0.4 Visualisation & EDA | T1 | Published |
| 0.5 Data splitting | T1 | Published |
| 1.1 Descriptive statistics | T1 | Published |
| 1.2 Relationships between variables | T1 | Published |
| 1.3 Probability essentials | T1 | Published |
| 1.4 Statistical inference | T1 | Published |
| 1.5 Resampling intuition | T1 | Published |
| 2.1 The regression problem | T1 | Published |
| 2.2 Simple linear regression | T1 | Published |
| 2.3 Accuracy of the coefficients | T1 | Published |
| 2.4 Accuracy of the full model | T1 | Published |
| 2.5 Multiple linear regression | T1 | Published |
| 2.6 Categorical predictors | T1 | Published |
| 2.7 Interaction terms | T1 | Published |
| 2.8 Nonlinear feature transformations | T1 | Published |
| 2.9 KNN regression | T1 | Published |
| 2.10 Regression assumptions & diagnostics | T1 | Published |
| 3.1 Classification fundamentals | T1 | Published |
| 3.1.5 AUPRC for skewed datasets | T1 | Published |
| 3.2 Why not linear regression for categories? | T1 | Published |
| 3.3 Logistic regression | T1 | Published |
| 3.4 Generative classifiers (LDA, QDA, NB) | T1 | Published |
| 3.5 KNN classification | T1 | Published |
| 3.6 Generalized linear models | T1 | Published |
| 3.7 Classification model comparison | T1 | Published |
| 4.1 The generalization problem | T1 | Published |
| 4.2 The validation set approach | T1 | Published |
| 4.3 Cross-validation | T1 | Published |
| 4.4 The bias–variance trade-off | T1 | Published |
| 4.5 The bootstrap | T1 | Published |
| 4.6 Hyperparameter tuning | T1 | Published |
| Part 5 — Regularization & high dimensions (6 pages) | T1 | Not started (5.1 stub) |
| Part 6 — Nonlinear regression (7 pages) | T1 | Not started |
| Part 7 — Trees & ensembles (7 pages) | T1 | Not started |
| Part 8 — SVMs (6 pages) | T1 | Not started |
| Part 9 — Unsupervised (9.1–9.6 T1; 9.7 T3) | mixed | Not started (stubs) |
| Part 10 — Deep learning (10.x) | T3 | Not started |
| Part 11 — Survival analysis (11.x) | T1 | Not started |
| Part 12 — Multiple testing (12.1–12.5 T1; 12.6 T2) | mixed | Not started (stubs) |
| Part 13 — LLMs (13.1–13.4, 13.7–13.8 T1; 13.5–13.6 T3) | mixed | Not started |
| Appendix A — Deriving the formulas | T1 | Not started |

## Tooling notes

- `verify_cells.py` (repo root) extracts every `{pyodide}` block from all pages and executes
  it in a shared namespace per page — the same smoke test used before each publish.
- The conda `quarto` package launcher expects `QUARTO_SHARE_PATH=$CONDA_PREFIX/share/quarto`
  if you call the binary without `conda activate`.
