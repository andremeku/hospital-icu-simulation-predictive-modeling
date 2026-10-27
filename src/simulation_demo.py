"""Illustrative stochastic ICU capacity demo; NOT the historical AnyLogic model.

Arrival rate and length-of-stay shape/scale default to nominal figures from
an academic report. Results depend on the random seed and simplifying assumptions.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import log

import numpy as np


@dataclass(frozen=True)
class Summary:
    arrivals: int
    admissions: int
    refusals: int
    average_occupancy_fraction: float
    avg_admitted_los_days: float | None


def simulate(days: int, capacity: int, arrival_rate: float, los_shape: float,
             los_scale: float, seed: int) -> Summary:
    if days <= 0 or capacity <= 0 or arrival_rate < 0 or los_shape <= 0 or los_scale <= 0:
        raise ValueError("Invalid simulation parameters")
    rng = np.random.default_rng(seed)
    # Occupied beds hold individual remaining lengths of stay, measured in days.
    occupied: list[int] = []
    occupancy = []
    arrivals_total = admissions = refusals = 0
    admitted_los = []
    for day in range(days):
        if day:
            occupied = [d - 1 for d in occupied if d - 1 > 0]
        today = int(rng.poisson(arrival_rate))
        arrivals_total += today
        for _ in range(today):
            if len(occupied) >= capacity:
                refusals += 1
            else:
                los = max(1, int(np.ceil(rng.lognormal(mean=log(los_scale), sigma=los_shape))))
                occupied.append(los)
                admitted_los.append(los)
                admissions += 1
        occupancy.append(len(occupied) / capacity)
    return Summary(arrivals_total, admissions, refusals,
                   float(np.mean(occupancy)),
                   float(np.mean(admitted_los)) if admitted_los else None)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--days", type=int, default=365)
    p.add_argument("--beds", type=int, default=15)
    p.add_argument("--arrival-rate", type=float, default=1.15)
    p.add_argument("--los-shape", type=float, default=0.883)
    p.add_argument("--los-scale", type=float, default=5.17)
    args = p.parse_args()
    result = simulate(args.days, args.beds, args.arrival_rate,
                      args.los_shape, args.los_scale, args.seed)
    print("ILLUSTRATIVE simulation only — not historical AnyLogic results")
    print(f"Simulated arrivals: {result.arrivals}")
    print(f"Simulated admissions: {result.admissions}")
    print(f"Simulated refusals: {result.refusals}")
    print(f"Average occupancy: {result.average_occupancy_fraction:.1%}")
    if result.avg_admitted_los_days is not None:
        print(f"Sample mean admitted LOS: {result.avg_admitted_los_days:.2f} days")


if __name__ == "__main__":
    main()
