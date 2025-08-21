#!/usr/bin/env python3

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"


def ensure_dirs() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def load_energy() -> pd.DataFrame:
    energy_path = RAW_DIR / "owid-energy-data.csv"
    df = pd.read_csv(energy_path)
    # Normalize column names (keep as-is, just ensure expected exist)
    expected_cols = [
        "country",
        "year",
        "nuclear_share_energy",
        "renewables_share_energy",
        "fossil_share_energy",
        "low_carbon_share_energy",
        "primary_energy_consumption",
    ]
    missing = [c for c in expected_cols if c not in df.columns]
    if missing:
        raise RuntimeError(
            f"Missing expected columns in energy dataset: {missing}. Update processing logic."
        )
    return df


def select_region(df: pd.DataFrame, names: list[str]) -> pd.DataFrame:
    present = [n for n in names if n in set(df["country"]) ]
    if not present:
        raise RuntimeError(f"None of the region names found in dataset: {names}")
    region_name = present[0]
    region_df = df[df["country"] == region_name].copy()
    region_df.insert(0, "region", region_name)
    return region_df


def build_eu_us_energy(df: pd.DataFrame) -> pd.DataFrame:
    eu_df = select_region(df, ["European Union (27)", "European Union"]) 
    us_df = select_region(df, ["United States"]) 

    keep_cols = [
        "region",
        "year",
        "nuclear_share_energy",
        "renewables_share_energy",
        "fossil_share_energy",
        "low_carbon_share_energy",
        "primary_energy_consumption",
    ]
    eu_df = eu_df[keep_cols].copy()
    us_df = us_df[keep_cols].copy()

    eu_df["region"] = "EU27"
    us_df["region"] = "US"

    combined = pd.concat([eu_df, us_df], ignore_index=True)
    combined.sort_values(["region", "year"], inplace=True)
    return combined


def write_outputs(df: pd.DataFrame) -> None:
    ensure_dirs()
    out_csv = PROCESSED_DIR / "eu_us_energy.csv"
    df.to_csv(out_csv, index=False)

    meta = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "sources": {
            "owid_energy": "https://github.com/owid/energy-data",
            "owid_co2": "https://github.com/owid/co2-data",
        },
        "notes": "Shares are OWID-provided shares of primary energy. EU is taken from the aggregated European Union entity if present.",
    }
    (PROCESSED_DIR / "metadata.json").write_text(json.dumps(meta, indent=2))


def main() -> int:
    energy = load_energy()
    combined = build_eu_us_energy(energy)
    write_outputs(combined)
    print("Processed dataset written to data/processed/eu_us_energy.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


