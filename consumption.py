"""Compute consumption from cumulative meter readings."""
import csv
from collections import defaultdict

UNIT = "kWh"


def load_readings(path):
    """Read a CSV file with columns: pdr, reading_date, reading_value."""
    with open(path, newline="", encoding="utf-8") as f:
        return [
            {
                "pdr": row["pdr"],
                "reading_date": row["reading_date"],
                "reading_value": float(row["reading_value"]),
            }
            for row in csv.DictReader(f)
        ]


def compute_consumption(readings):
    """Return the consumption between consecutive readings of each PDR.

    Readings are cumulative: consumption = current value - previous value.
    """
    by_pdr = defaultdict(list)
    for r in readings:
        by_pdr[r["pdr"]].append(r)

    result = []
    for pdr, rows in by_pdr.items():
        rows.sort(key=lambda r: r["reading_date"])
        for prev, curr in zip(rows, rows[1:]):
            consumption = curr["reading_value"] - prev["reading_value"]
            if consumption < 0:
                # Negative value: meter replacement or reset, skip it
                continue
            result.append(
                {
                    "pdr": pdr,
                    "period_end": curr["reading_date"],
                    "consumption": consumption,
                }
            )
    return result


def main():
    readings = load_readings("readings.csv")
    for row in compute_consumption(readings):
        print(f"{row['pdr']} {row['period_end']} {row['consumption']:.1f} {UNIT}")


if __name__ == "__main__":
    main()
