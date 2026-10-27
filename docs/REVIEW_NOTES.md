# Project 3 — Source review notes

These observations compare the four files in the uploaded ZIP. No clinical source dataset was included; the supplied materials alone cannot validate model estimates or reproduce data-derived results.

## Inventory

- `original_analysis.ipynb`: Original Colab notebook, **two code cells** and stored outputs; code is preserved in `archive/` with displayed outputs cleared.
- `ICU_Capacity_Model.alp`: AnyLogic model file, created with **AnyLogic 8.9.4** according to its XML header.
- `separate_3d_assets.zip`: 3D `.dae` assets for the AnyLogic model; third-party rights not established.
- `group_project_report.pdf`: 12-page group report, submitted April 30, 2025.

## Cross-artifact discrepancies (not corrected silently)

- The report states **6,228 original records**, while one original Colab output says **6,229 after cleaning**. Another Colab run filtered to **2,403 records with valid dates**. Those represent different processing paths.
- The PDF calculates **1.15 admissions/day** by dividing 420 by 365. Colab prints **1.67/day** from `mean()` over days with recorded admissions; days without recorded admissions are excluded from that average.
- The report gives multiple ICU simulation utilization figures: **86.1%**, and later **~94%**. Two saved Colab executions report **97.0% and 95.4%**.
- The report's algorithm comparison says **Random Forest ROC-AUC 0.93**, but the saved runs show materially different numbers, including **~0.81**. There is insufficient provenance to reproduce or reconcile them.
- The original Python code uses `np.random.lognormal(shape, scale)`. NumPy interprets these as the **underlying normal mean and standard deviation**, whereas the SciPy `lognorm.fit` parameters are **shape and scale**. Those conventions are not interchangeable. The separately prepared demonstration script uses `lognormal(mean=log(scale), sigma=shape)`.
- The notebook creates its label from combinations of `bad` and `last`. The supplied materials do not independently establish that this construction is a validated definition of **discharge readiness**.
- The original notebook uses a row-wise random train/test split, despite multiple rows belonging to patients or stays, so leakage is possible. The report mentions five-fold cross-validation, but that is not demonstrated by the saved Python code.

## What was changed in this portfolio copy

- Stripped only saved execution outputs from the **archived notebook** to reduce patient-level exposure. Code cells are not rewritten.
- Added **new, separately labeled** descriptive and simulation examples in `src/` that are portable and do not masquerade as original results.
- Omitted the clinical dataset (not present), the 3D model assets, and the original group report. The AnyLogic .alp project is included, but was not execution-tested.

These are academic/technical review notes, **not clinical advice**.
