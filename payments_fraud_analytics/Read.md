Payments & Fraud Analytics

Project Overview

This project is Part 1 of the Paytm FinTech Analytics & AI Platform Capstone. It demonstrates a complete payments analytics workflow, including synthetic data generation, payment reconciliation, SQL-based fraud detection, spreadsheet analysis, and dashboard visualization.
________________________________________
Folder Structure
payments_fraud_analytics/
│
├── generate_data.py
├── merchants.csv
├── users.csv
├── ledger.csv
├── gateway_export.csv
├── reconcile.py
├── dashboard.py
├── sql_queries.sql
├── paytm_payments.db
├── merchant_workbook.xlsx
├── charts/
│   ├── daily_gmv.png
│   ├── daily_chargebacks.png
│   ├── payment_method.png
│   ├── category.png
│   └── top10_merchants.png
└── README.md
________________________________________
Requirements
Install the required Python libraries:
pip install pandas numpy matplotlib openpyxl
________________________________________
Running the Project

Step 1 – Generate Data

Run the data generation script:

python generate_data.py

This creates:

•	merchants.csv

•	users.csv

•	ledger.csv

•	gateway_export.csv

________________________________________
Step 2 – Create SQLite Database

Create a SQLite database named:

paytm_payments.db

Import:

•	merchants.csv

•	users.csv

•	ledger.csv

________________________________________
Step 3 – Execute SQL Queries

Run the queries from: 

sql_queries.sql

The queries perform:

•	Chargeback analysis

•	Burner account detection

•	Velocity attack detection

•	Merchant performance analysis

•	Daily GMV analysis

•	Payment method analysis

•	LEFT JOIN demonstration

________________________________________
Step 4 – Payment Reconciliation

Run:

python reconcile.py

The script compares the ledger and gateway data and generates:

•	missing_in_gateway.csv

•	missing_in_ledger.csv

•	amount_mismatches.csv

•	status_mismatches.csv

________________________________________
Step 5 – Dashboard

Run:

python dashboard.py

The dashboard generates:

•	Daily GMV Trend

•	Daily Chargeback Trend

•	GMV by Payment Method

•	GMV by Category

•	Top 10 Merchants Table

All charts are saved inside the charts/ folder.
________________________________________
Spreadsheet Tasks

The workbook merchant_workbook.xlsx contains:

•	VLOOKUP for merchant information

•	HLOOKUP demonstration

•	Nested IF classification

•	Pivot Table summarizing transactions

•	Merchant-wise transaction analysis
________________________________________
Dashboard Interpretation

Headline KPIs

The dashboard displays:

•	Total GMV

•	Success Rate

•	Chargeback Ratio

•	Reconciliation Match Rate

These metrics provide a high-level overview of payment system performance.

Daily GMV

The Daily GMV chart shows transaction value trends over time and helps identify high-volume business days.

Daily Chargebacks

This chart highlights the number of chargeback transactions each day and can indicate potential fraud spikes.

Payment Method Analysis

The payment method chart compares transaction values across UPI, Wallet, Card, and Netbanking.

Category Analysis

The category chart compares GMV across merchant categories to identify the strongest business segments.

Top Merchants

The Top 10 Merchants table ranks merchants by transaction volume and highlights chargeback ratios to identify high-risk merchants.

________________________________________
Design Decisions

•	Synthetic data is generated using a fixed random seed to ensure reproducible results.

•	SQL queries are normalized across separate Merchants, Users, and Transactions tables.

•	Payment reconciliation uses transaction IDs as the primary matching key.

•	Dashboard visualizations are generated using Python and Matplotlib.

•	Merchant details are merged using VLOOKUP in the spreadsheet and joins in SQL/Python.

________________________________________
Technologies Used

•	Python

•	Pandas

•	NumPy

•	Matplotlib

•	SQLite

•	Microsoft Excel / Google Sheets
________________________________________
Author
Prepared as part of the Paytm FinTech Analytics & AI Platform Capstone Project.
