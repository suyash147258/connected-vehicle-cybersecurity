# Offline CAN-Log Checker

Defensive, offline-only baseline anomaly checker for CAN logs (no vehicle
connection, no frame transmission). Findings are indicators, not proof of attack.

## Run
    python3 src/can_log_checker.py data/sample_can_log.csv \
        --allowlist data/allowlist.txt --window 1.0 --rate-threshold 20

Options: `--max-dlc 64` for CAN FD logs. Exit code 1 if findings, 0 if clean.
Requires Python 3.8+, no external dependencies.

## CSV format
    timestamp,can_id,dlc,data
Derive allowlist and thresholds from your real vehicle architecture.
