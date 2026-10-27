"""Descriptive exploration of *authorized local* ICU data; not a clinical tool.

Usage: python src/descriptive_analysis.py --input PATH --output summary.json
This deliberately does not export identifiable records.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats


def summarize(path: Path) -> dict:
    df = pd.read_csv(path, sep=";")
    df.columns = df.columns.str.strip()
    df = df.rename(columns={"dayIn": "day_in"})
    needed = {"codes", "id", "dates", "day_in"}
    missing = sorted(needed - set(df.columns))
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")
    rows_in = len(df)
    df = df.drop_duplicates().copy()
    df["day_in"] = pd.to_numeric(df["day_in"], errors="coerce")
    df["dates"] = pd.to_datetime(df["dates"], errors="coerce")
    df = df.dropna(subset=["codes", "id", "day_in"])
    df = df.loc[df["day_in"] >= 1]
    stays = (df.groupby(["codes", "id"], dropna=False)["day_in"]
               .max().rename("los_days").reset_index())
    if stays.empty:
        raise ValueError("No valid ICU stay rows found")
    arrivals = df.loc[(df["day_in"] == 1) & df["dates"].notna(), "dates"].dt.normalize()
    if arrivals.empty:
        daily_mean = None
        zero_day_message = "No parseable admission dates"
    else:
        # Explicit denominator: calendar span from first to last observed admission date.
        counts = arrivals.value_counts().sort_index()
        calendar = pd.date_range(counts.index.min(), counts.index.max(), freq="D")
        daily_mean = float(counts.reindex(calendar, fill_value=0).mean())
        zero_day_message = "Includes zero-admission dates within observed date range"
    lognormal = None
    positive_los = stays.loc[stays["los_days"] > 0, "los_days"]
    if len(positive_los) > 1 and positive_los.nunique() > 1:
        shape, _, scale = stats.lognorm.fit(positive_los, floc=0)
        lognormal = {"shape": float(shape), "scale": float(scale)}
    n_stays_per_patient = stays.groupby("codes")["id"].nunique()
    return {
        "input_rows": int(rows_in),
        "valid_rows_after_dedup_and_filter": int(len(df)),
        "unique_patients": int(stays["codes"].nunique()),
        "unique_stays": int(len(stays)),
        "mean_length_of_stay_days": float(stays["los_days"].mean()),
        "fraction_patients_with_multiple_stays": float((n_stays_per_patient > 1).mean()),
        "daily_admission_mean_observed_span": daily_mean,
        "admission_denominator_note": zero_day_message,
        "lognormal_los_fit": lognormal,
        "warning": "Exploratory descriptive values only; do not use for clinical decisions.",
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--output", type=Path)
    args = p.parse_args()
    summary = summarize(args.input)
    rendered = json.dumps(summary, indent=2, allow_nan=False)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
