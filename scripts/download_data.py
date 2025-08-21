#!/usr/bin/env python3

import os
import sys
from pathlib import Path
from typing import Dict

import requests


DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"

DATASETS: Dict[str, str] = {
    "owid-energy-data.csv": "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv",
    "owid-co2-data.csv": "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv",
}


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def download_file(url: str, dest: Path) -> None:
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    dest.write_bytes(response.content)


def main() -> int:
    ensure_dir(DATA_DIR)
    for filename, url in DATASETS.items():
        dest_path = DATA_DIR / filename
        print(f"Downloading {url} -> {dest_path}")
        try:
            download_file(url, dest_path)
        except Exception as exc:  # noqa: BLE001
            print(f"Failed to download {url}: {exc}", file=sys.stderr)
            return 1
    print("All datasets downloaded.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


