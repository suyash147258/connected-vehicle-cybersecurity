# Research Methodology

## 1. Introduction

The methodology adopted for this project focuses on examining cybersecurity verification techniques for Controller Area Network (CAN) communication in connected vehicles. The project combines academic research with a Python-based offline demonstration to understand how CAN log data can be analyzed for potential irregularities.

## 2. Research Approach

The project follows a research-oriented and implementation-based approach consisting of the following stages:

1. Study of connected vehicle communication and CAN bus architecture.
2. Identification of cybersecurity concerns associated with CAN communication.
3. Review of existing research articles and security verification techniques.
4. Development of a Python-based CAN log verification script.
5. Testing the implementation using a sample CAN log dataset.
6. Analysis of the verification output and identification of limitations.

## 3. Dataset Preparation

A sample CAN log dataset in CSV format is used as the input for the demonstration.

The repository contains a synthetic dataset designed to demonstrate the verification process. It does not represent actual vehicle communication data.

The dataset is stored in:

`data/sample_can_log.csv`

## 4. Implementation Methodology

The verification process is implemented using Python.

The `can_log_checker.py` script processes the supplied CSV file and applies configurable verification criteria.

The implemented approach includes:

- **CAN ID Allowlisting:** Checks CAN identifiers against a configured list of permitted identifiers.
- **Message Frequency Verification:** Uses configurable message-per-second thresholds to examine CAN message frequency.
- **Log Validation:** Processes the input records and identifies entries that do not satisfy the configured verification criteria.

## 5. Testing and Analysis

The Python implementation is executed using the sample CAN log dataset.

Different configuration parameters can be supplied during execution to demonstrate how verification criteria affect the analysis.

The resulting output is examined to understand which records satisfy or violate the configured conditions.

## 6. Tools and Technologies

| Tool / Technology | Purpose |
|---|---|
| Python 3 | CAN log processing and verification |
| CSV | Dataset storage |
| LaTeX | Academic research article preparation |
| GitHub | Source code management and project documentation |

## 7. Limitations

The current implementation is an offline demonstration that analyzes CSV-based CAN log data.

It does not directly capture live CAN bus traffic, communicate with an Electronic Control Unit (ECU), or perform real-time vehicle intrusion detection.

The demonstration dataset is synthetic, and its results should not be interpreted as validation on a real vehicle.

## 8. Future Scope

Potential extensions of this project include:

- Integration with physical CAN bus interfaces for live traffic acquisition.
- Development of real-time CAN message monitoring.
- Implementation of advanced anomaly detection techniques.
- Evaluation using real-world CAN traffic datasets.
- Exploration of machine learning-based intrusion detection methods.

## 9. Conclusion

The adopted methodology provides a structured approach to studying connected vehicle cybersecurity and demonstrating basic CAN log verification through Python. The combination of academic research and software implementation establishes a foundation for further investigation into CAN communication security.
