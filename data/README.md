# Data availability

The ZIP uploaded for this project **did not include** the original clinical patient-record CSV (`DataForClass.csv` is named in the original notebook's stored outputs). Patient-level ICU records are **not** included in this public-review package.

For the portable descriptive script, the input should be a semicolon-delimited CSV containing at least:

| Column | Description |
| --- | --- |
| `codes` | Patient code; potentially sensitive, keep local |
| `id` | Stay/session identifier; potentially sensitive, keep local |
| `dates` | Date field used by original analysis |
| `dayIn` or `day_in` | Patient day number during ICU stay |

The original exploratory classifier also refers to `age`, `gender`, `SAPS`, `Glasgow`, `TISS`, `PA`, `FC`, `Temp`, `bad`, and `last`.

**Do not upload patient records or individually identifying outputs.** The repository's `.gitignore` excludes raw data files in `data/`, but this is not a privacy control for uploads made through the GitHub browser.
