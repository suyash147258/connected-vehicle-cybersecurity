#!/usr/bin/env python3
"""
Offline CAN log sanity checker for an academic demonstration.

Input CSV columns:
    timestamp,can_id,dlc,data

This tool only reads a file. It does not connect to a CAN interface or transmit
frames. Defaults are illustrative and must be tuned for a specific vehicle.
"""
import argparse
import csv
from collections import defaultdict

DEFAULT_ALLOWED_IDS = {"0x100", "0x101", "0x120", "0x180", "0x200"}

def normalize_can_id(value):
    value = value.strip().lower()
    return value if value.startswith("0x") else "0x" + value

def inspect(path, allowed_ids, max_per_second):
    counts = defaultdict(int)
    findings = []
    with open(path, "r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        required = {"timestamp", "can_id", "dlc", "data"}
        if not reader.fieldnames or not required.issubset(set(reader.fieldnames)):
            raise ValueError("CSV must contain timestamp,can_id,dlc,data columns")

        rows = list(reader)
        for line_number, row in enumerate(rows, start=2):
            can_id = normalize_can_id(row["can_id"])
            try:
                timestamp = float(row["timestamp"])
                dlc = int(row["dlc"])
            except (TypeError, ValueError):
                findings.append((line_number, "INVALID_FIELD",
                                 "Timestamp or DLC is not numeric"))
                continue

            if can_id not in allowed_ids:
                findings.append((line_number, "UNKNOWN_CAN_ID",
                                 "Identifier {} is not in the configured allowlist".format(can_id)))

            if dlc < 0 or dlc > 8:
                findings.append((line_number, "INVALID_CLASSICAL_CAN_DLC",
                                 "DLC {} is outside classical CAN range 0..8".format(dlc)))

            second_bucket = int(timestamp)
            counts[(can_id, second_bucket)] += 1
            if counts[(can_id, second_bucket)] == max_per_second + 1:
                findings.append((line_number, "RATE_THRESHOLD",
                                 "{} exceeded {} frames in second {}".format(
                                     can_id, max_per_second, second_bucket)))

    return len(rows), findings

def main():
    parser = argparse.ArgumentParser(description="Offline CAN CSV anomaly checks")
    parser.add_argument("csv_file", help="Path to an offline CAN log CSV")
    parser.add_argument("--max-per-second", type=int, default=5,
                        help="Illustrative per-ID per-second threshold (default: 5)")
    parser.add_argument("--allow", default=",".join(sorted(DEFAULT_ALLOWED_IDS)),
                        help="Comma-separated CAN IDs, e.g. 0x100,0x101")
    args = parser.parse_args()

    allowed = {normalize_can_id(item) for item in args.allow.split(",") if item.strip()}
    total, findings = inspect(args.csv_file, allowed, args.max_per_second)
    print("Rows inspected: {}".format(total))
    print("Findings: {}".format(len(findings)))
    for line, code, detail in findings:
        print("Line {} [{}] {}".format(line, code, detail))
    if not findings:
        print("No configured checks were triggered.")
    print("\nNote: findings are indicators for investigation, not proof of an attack.")

if __name__ == "__main__":
    main()
