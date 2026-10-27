# Hospital ICU Simulation & Predictive Modeling

**Stochastic Processes | KEDGE Business School | Academic team project (April 2025)**

**Project authors:** **Andre Kurniawan and project partner**. This was a collaborative academic project; the repository does not claim sole authorship or clinical approval.

## Project overview

This study investigated how **patient arrivals, length of stay, and readmissions** interact with intensive-care capacity. It combines:

1. **Exploratory ICU data analysis** to estimate arrival rates, lengths of stay, and return rates.
2. **Discrete-event simulation in AnyLogic** to illustrate a 15-bed ICU and track utilization and admission refusals.
3. **Exploratory classification benchmarks** using Logistic Regression, Decision Tree, Random Forest, SVM, and k-NN on recorded patient metrics.

The original report's intended use was ICU capacity planning and discharge-related decision support. **The predictive target definition and evaluation protocol have not been clinically validated; the code and reported results must not be used to make patient care or discharge decisions.**

## At a glance — original project report

| Item | As reported in the 2025 group report |
| --- | --- |
| Historical data period | January 2018–December 2019 |
| Original records | 6,228 |
| Unique patient identifiers / stays mentioned | 707 patients / 845 stays |
| Modeled ICU | 15 beds, 15 nurses |
| Estimated arrivals | 1.15 patients/day (report) |
| Average length of stay | 7.48 days (report) |
| Return rate | 13.58% (report) |
| Simulated utilization | 86.1% in the KPI section; approximately 94% elsewhere in the report |
| Example model comparison | Random Forest ROC-AUC 0.93 in the report's summary table |

**Important: the source artifacts disagree.** One saved notebook run reports **1.67 arrivals/day**, **95.4% utilization**, **542 rejections** and **Random Forest ROC-AUC around 0.81**; the PDF gives different simulation/model metrics. The README reports these as **historical outputs, not verified findings**. Differences may reflect filtering, labels, random simulation runs, or separate experiment settings; no single explanation is established. See [Review notes](docs/REVIEW_NOTES.md).

## Original workflow

`Historical ICU records → data cleaning → patient-flow parameters → AnyLogic bed-capacity simulation → exploratory model comparison → discussion of operational and ethical limitations`

The team modeled arrivals, bed/nurse availability, ICU stays, readmissions, utilization, and rejected arrivals. A separate Python notebook estimated parameters, ran an hourly illustrative simulation, and explored classification.

## Technologies

`Python` · `pandas` · `NumPy` · `SciPy` · `Matplotlib` · `scikit-learn` · `Jupyter/Google Colab` · `AnyLogic 8.9.4`

## Repository layout

```text
hospital-icu-simulation-predictive-modeling/
├── README.md
├── anylogic/
│   ├── ICU_Capacity_Model.alp
│   └── README.md
├── archive/
│   └── original_analysis.ipynb
├── data/
│   └── README.md
├── docs/
│   ├── REVIEW_NOTES.md
│   └── REPRODUCIBILITY.md
├── src/
│   ├── descriptive_analysis.py
│   └── simulation_demo.py
├── figures/
│   └── README.md
├── requirements.txt
└── .gitignore
```

- **`anylogic/`**: Original AnyLogic 8.9.4 model source (`.alp`). The referenced 3D Collada assets are not included pending license checks, so some visuals may be missing. See [AnyLogic notes](anylogic/README.md).
- **`archive/`**: Two code cells from the original Colab notebook; execution output cleared for privacy. Original code still needs Colab and the missing data file.
- **`src/descriptive_analysis.py`**: A separately prepared, command-line-friendly descriptive workflow (not a claim to reproduce the report numbers).
- **`src/simulation_demo.py`**: A separately prepared reproducible **illustrative** simulation using nominal report parameters (not a reconstruction of AnyLogic behavior).
- **`data/`**: Input-data requirements; **clinical source data are not included**.
- **`figures/`**: Space for figures generated from data that may lawfully be shared.

The original **AnyLogic `.alp` model is included** as a viewable project artifact. The associated 3D `.dae` assets and full group report are not included in this release. Confirm collaborator permission for the `.alp` and licenses for any third-party 3D assets before making this repository public. The AnyLogic model has **not been run or verified** in AnyLogic in this packaging step.

## Try the reproducible, non-clinical simulation example

```bash
pip install -r requirements.txt
python src/simulation_demo.py --seed 42 --days 365 --beds 15
```

This example uses parameters stated in the historical report and is **not** expected to reproduce its numerical KPIs. It prints simulated occupancy/refusals and writes no patient information.

## Run descriptive analysis on an **authorized** local dataset

```bash
python src/descriptive_analysis.py --input /path/to/authorized_data.csv --output summary.json
```

The original notebook expects a semicolon-delimited CSV with columns including `dates`, `dayIn`, `codes`, and `id`. Neither the dataset nor clinically meaningful target labels are provided in this repository. See [Data requirements](data/README.md) and [Reproducibility](docs/REPRODUCIBILITY.md).

## Key learning outcomes

- Translating empirical arrival and stay data into stochastic-process assumptions.
- Exploring ICU bottlenecks under a constrained-bed capacity model.
- Comparing classification models while examining data-cleaning and evaluation limitations.
- Presenting analytical results with **patient safety, uncertainty, and human oversight** in mind.

## Data privacy & academic attribution

This work concerns clinical records. **Never commit patient-level data, patient identifiers, notebook outputs containing individual records, access credentials, or restricted course materials** to a public GitHub repository. Sharing the group report or AnyLogic assets also requires confirmation of coauthor rights and any embedded third-party asset licenses.

**Disclaimer:** Educational research artifact only. Not a medical device or operational recommendation; no clinical accuracy, GDPR compliance, or suitability for patient care is certified by this repository.
