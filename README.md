# ML, Statistics & LLM — Interactive Course

An interactive machine-learning, statistics, and LLM course (with a biological-data thread), built with [Quarto Live](https://github.com/r-wasm/quarto-live) and hosted on **GitHub Pages**. All code cells run **in the browser** (Pyodide/webR) — designed first for reading in **Safari on iPad**.

**Live site:** https://enduringchung.github.io/ml-interactive-course/

## Structure

```
_quarto.yml                    site config (format: live-html, engine: markdown)
index.qmd                      course home: how-to, tier legend, course map
part-00-python-foundations/    00-1 … 00-5   (T1)
part-01-statistics-bridge/     01-1 … 01-5   (T1)
notebooks/                     Colab companion notebooks for T3 pages (Part 10 …)
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
| 5.1 Feature selection | T1 | Published |
| 5.2 Ridge regression | T1 | Published |
| 5.3 Lasso regression | T1 | Published |
| 5.4 Elastic net | T1 | Published |
| 5.5 PCR and PLS | T1 | Published |
| 5.6 High-dimensional data | T1 | Published |
| 6.1 Polynomial regression | T1 | Published |
| 6.2 Step functions | T1 | Published |
| 6.3 Basis functions | T1 | Published |
| 6.4 Regression splines | T1 | Published |
| 6.5 Smoothing splines | T1 | Published |
| 6.6 Local regression | T1 | Published |
| 6.7 Generalized additive models | T1 | Published |
| 7.1 Decision trees | T1 | Published |
| 7.2 Advantages & limitations of trees | T1 | Published |
| 7.3 Bagging | T1 | Published |
| 7.4 Random forests | T1 | Published |
| 7.5 Gradient boosting | T1 | Published |
| 7.6 Modern boosting libraries | T1 | Published |
| 7.7 Bayesian additive regression trees | T1 | Published |
| 8.1 Geometry essentials | T1 | Published |
| 8.2 Maximal-margin classifier | T1 | Published |
| 8.3 Soft-margin classifier | T1 | Published |
| 8.4 Kernel SVM | T1 | Published |
| 8.5 SVM vs logistic regression | T1 | Published |
| 8.6 Multiclass SVM | T1 | Published |
| 9.1 The unsupervised mindset | T1 | Published |
| 9.2 Principal component analysis | T1 | Published |
| 9.3 Missing values & matrix completion | T1 | Published |
| 9.4 K-means clustering | T1 | Published |
| 9.5 Hierarchical clustering | T1 | Published |
| 9.6 Practical clustering issues | T1 | Published |
| 9.7 UMAP / t-SNE / autoencoders | T3 | Not started (T3 pass) |
| 10.1 PyTorch foundations | T3 | Draft (verified cells) |
| 10.2 Single-layer neural networks | T3 | Draft (verified cells) |
| 10.3 Multilayer neural networks | T3 | Draft (verified cells) |
| 10.4 Gradient descent & backpropagation | T1 (+T3 torch lab) | Draft (verified cells) |
| 10.5 Regularization for neural networks | T3 | Draft (verified cells) |
| 10.6 Convolutional neural networks | T3 | Draft (verified cells) |
| 10.7 Recurrent neural networks | T3 | Draft (verified cells) |
| 10.8 LSTM and GRU | T3 | Draft (verified cells) |
| 10.9 Attention and transformers | T3 | Draft (verified cells) |
| 10.10 When deep learning is appropriate | T1 | Draft (verified cells) |
| 11.1 Why survival data is special | T1 | Published |
| 11.2 Kaplan–Meier survival curves | T1 | Published |
| 11.3 Log-rank test | T1 | Published |
| 11.4 Hazard functions | T1 | Published |
| 11.5 Cox proportional hazards | T1 | Published |
| 12.1 Hypothesis-test review | T1 | Published |
| 12.2 Why multiple testing is dangerous | T1 | Published |
| 12.3 Family-wise error rate | T1 | Published |
| 12.4 False discovery rate | T1 | Published |
| 12.5 Resampling for p-values and FDR | T1 | Published |
| 12.6 Differential-expression workflow | T2 | Published (stub — frozen output pass pending) |
| 13.1 LLM foundations | T1 | Published (verified cells) |
| 13.2 Transformer architecture | T1 | Published (verified cells) |
| 13.3 Training pipeline | T1 | Published (verified cells) |
| 13.4 Model families and variants | T1 | Published (verified cells) |
| 13.5 Local deployment | T3 | Published (verified cells + Colab lab) |
| 13.6 Customization (RAG, LoRA, agents) | T3 | Published (verified cells + Colab lab) |
| 13.7 Evaluation and limitations | T1 | Published (verified cells) |
| 13.8 Applications and next steps | T1 | Published (verified cells) |
| A.1 Normal equations for linear regression | T1 | Published (verified cells) |
| A.2 Why least squares is maximum likelihood | T1 | Published (verified cells) |
| A.3 Logistic regression: deriving the gradient | T1 | Published (verified cells) |
| A.4 Ridge regression: deriving the closed form | T1 | Published (verified cells) |
| A.5 Why lasso has no closed form | T1 | Published (verified cells) |
| A.6 PCA: deriving the first principal component | T1 | Published (verified cells) |
| A.7 AUPRC trapezoidal estimator, worked example | T1 | Published (verified cells) |

## Tooling notes

- `verify_cells.py` (repo root) extracts every `{pyodide}` block from all pages and executes
  it in a shared namespace per page — the same smoke test used before each publish.
- The conda `quarto` package launcher expects `QUARTO_SHARE_PATH=$CONDA_PREFIX/share/quarto`
  if you call the binary without `conda activate`.
