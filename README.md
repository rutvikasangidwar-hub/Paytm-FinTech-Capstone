# Paytm-FinTech-Capstone
Project Overview
This repository contains a three-part FinTech capstone project covering payments and fraud analytics, credit risk and lending machine learning, and AI advisory with blockchain-related risk analysis.
The project demonstrates an end-to-end workflow using Python, SQL, SQLite, spreadsheets, machine learning, anomaly detection, and AI-oriented financial analysis.
Repository Structure
```text
FinTech-Capstone/
│
├── README.md
│
├── payments_fraud_analytics/
│   ├── README.md
│   ├── generate_data.py
│   ├── merchants.csv
│   ├── users.csv
│   ├── ledger.csv
│   ├── gateway_export.csv
│   ├── reconcile.py
│   ├── dashboard.py
│   ├── sql_queries.sql
│   ├── paytm_payments.db
│   ├── merchant_workbook.xlsx
│   ├── missing_in_gateway.csv
│   ├── missing_in_ledger.csv
│   ├── amount_mismatches.csv
│   ├── status_mismatches.csv
│   └── charts/
│
├── credit_risk_lending_ml/
│   ├── README.md
│   ├── generate_data.py
│   ├── credit_applicants.csv
│   ├── txn_behaviour.csv
│   ├── credit_risk_model.py
│   ├── anomaly_results.csv
│   ├── bias_awareness_note.md
│   └── charts/
│       ├── 01_default_distribution.png
│       ├── 02_bureau_score_missing.png
│       ├── 03_feature_distributions.png
│       ├── 04_confusion_matrix_logistic.png
│       ├── 05_confusion_matrix_tree.png
│       ├── 06_roc_comparison.png
│       ├── 07_risk_tiers.png
│       └── 08_anomaly_detection.png
│
└── ai_advisory_blockchain/
    ├── README.md
    ├── stock_universe.py
    ├── investor_profiles.py
    ├── disclosure_snippets.py
    ├── advisory_agent.py
    ├── extract_disclosure.py
    ├── debate.py
    ├── dcf_calculator.py
    └── blockchain_risk_note.md
```
---
Part 1: Payments & Fraud Analytics

This section analyzes a simulated digital payments ecosystem.

Main components

Synthetic payment data generation

Merchant, user, and transaction datasets

Payment reconciliation between internal ledger and gateway data

SQL analysis using SQLite

Chargeback and fraud-related analysis

Burner-account and transaction-velocity detection

Excel-based merchant analysis

Dashboard visualizations for GMV, chargebacks, payment methods, categories, and top merchants

Key technologies

Python, Pandas, NumPy, Matplotlib, SQLite, SQL, and Excel.

Run:

```bash

python generate_data.py

python reconcile.py

python dashboard.py

```
See `payments_fraud_analytics/README.md` for detailed instructions.

---
Part 2: Credit Risk & Lending ML

This section develops and evaluates machine-learning approaches for credit default prediction and transaction anomaly detection.

Main components

Exploratory data analysis

Missing-value analysis

`is_thin_file` feature engineering

Stratified train/test split

Training-data-only preprocessing

Logistic Regression

Decision Tree classification

Accuracy, precision, recall, F1, ROC, and AUC evaluation

Risk-tier analysis using predicted probabilities

Isolation Forest anomaly detection

Bias-awareness and model-governance considerations

The anomaly analysis identified 15 injected anomalies, with 11 detected by the implemented Isolation Forest workflow, producing a recall of 73.33%.

See `credit_risk_lending_ml/README.md` for detailed instructions.

---

Part 3: AI Advisory & Blockchain

This section focuses on AI-assisted financial advisory workflows and blockchain-related risk analysis.

Main components

Stock universe definition

Investor-profile handling

Financial disclosure snippets

Advisory-agent logic

Disclosure extraction

Multi-perspective debate

DCF calculation

Blockchain risk note

See `ai_advisory_blockchain/README.md` for detailed instructions.

---

Installation

Install the main Python dependencies:

```bash

pip install pandas numpy matplotlib scikit-learn openpyxl

```

Depending on the Part 3 implementation, additional packages may be required. Refer to the relevant folder README for project-specific requirements.

How to Use This Repository

Clone or download the repository.

Open the required project folder.

Install the required dependencies.

Run the data-generation scripts where applicable.

Run the analysis or model scripts.

Review generated charts, CSV outputs, database files, and documentation.

Technologies Used

Python

Pandas

NumPy

Matplotlib

Scikit-learn

SQLite

SQL

Microsoft Excel / compatible spreadsheet software

Repository Organization

Each part is kept in a separate folder so that data, source code, outputs, charts, and documentation remain organized and easy to review.

Author

Prepared as a FinTech Analytics & AI Platform Capstone Project.

