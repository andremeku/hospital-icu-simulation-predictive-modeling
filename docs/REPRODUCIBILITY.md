# Reproducibility and scope

### What runs without real patient data?

`python src/simulation_demo.py --seed 42`: a self-contained, **illustrative stochastic simulation** initialized from nominal values described in the report. This does **not** reproduce AnyLogic nor the saved notebook simulation outputs.

### What requires authorized local data?

`python src/descriptive_analysis.py --input /path/to/file.csv`: descriptive processing only. The semicolon-separated CSV used for the original analysis was **not included in the uploaded project archive**. Records may contain health information; do not commit real clinical data.

The archived Colab notebook may require Google Colab, manual upload, and additional preprocessing. Its stored results were removed to avoid exposing individual-level data. Code is unchanged.

### What requires AnyLogic?

The `.alp` file records an AnyLogic 8.9.4 project. The renamed `.alp` model is included in this repository; the associated 3D files are retained separately and not published here. We have **not** executed or validated the AnyLogic model here. To reproduce original layouts, the user may need both `.alp` and the `.dae` assets plus the correct AnyLogic version.

### What is not independently verified?

Historical patient counts, fitted distribution diagnostics, discharge-classifier AUC, modeling thresholds, simulation KPIs and projected benefits of extra beds. See review notes for discrepancies across saved runs and report.
