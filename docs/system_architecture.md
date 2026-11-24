# System Architecture

## 1. Overview

The Connected Vehicle Cybersecurity project demonstrates an offline approach to verifying and analyzing Controller Area Network (CAN) log data. The system uses a Python-based verification script to examine CAN log entries and identify potential irregularities based on configurable validation parameters.

The architecture is designed as a lightweight software-based demonstration of cybersecurity verification concepts in connected vehicles.

## 2. System Architecture

The system consists of three primary components:

1. **CAN Log Dataset:** A CSV file containing sample CAN log records serves as the input to the verification system. The current repository includes a synthetic demonstration dataset.

2. **Python-Based Verification Module:** The `can_log_checker.py` script processes the input CSV file and performs verification checks. It supports configurable parameters, including message frequency thresholds and CAN ID allowlisting.

3. **Verification Output:** The script produces the results of its checks, helping identify records that may violate the configured validation criteria.

## 3. Data Flow

The overall workflow follows this sequence:

**CAN Log CSV → Python Data Processing → Verification Checks → Analysis Results**

- The system reads CAN log records from the supplied CSV file.
- The Python script processes the available records.
- Configurable verification rules are applied to examine the log data.
- The results are generated to demonstrate the verification process.

## 4. Software Components

| Component | Description |
|---|---|
| `data/sample_can_log.csv` | Synthetic CAN log dataset |
| `src/can_log_checker.py` | Python-based CAN log verification script |
| `main.tex` | LaTeX research article |
| `references.bib` | Bibliography database |

## 5. Architecture Scope and Limitations

The current implementation operates on offline CSV data rather than directly interfacing with a physical vehicle CAN bus. It does not perform real-time CAN traffic monitoring or directly control vehicle systems.

The project serves as an academic demonstration of CAN log verification and connected vehicle cybersecurity concepts, with scope for future development towards real-time CAN communication monitoring and advanced intrusion detection techniques.
