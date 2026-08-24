Payments & Fraud Analytics
Project Overview
This project analyzes a simulated payments ecosystem and demonstrates data generation, payment reconciliation, SQL analysis, fraud detection, spreadsheet analysis, and dashboard reporting.
Folder Structure
```text
payments_fraud_analytics/
├── README.md
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
├── missing_in_gateway.csv
├── missing_in_ledger.csv
├── amount_mismatches.csv
├── status_mismatches.csv
└── charts/
    ├── 01_daily_gmv.png
    ├── 02_daily_chargebacks.png
    ├── 03_payment_method.png
    ├── 04_category.png
    └── 05_top10_merchants.png
```
Requirements
```bash
pip install pandas numpy matplotlib openpyxl
```
How to Run
1. Generate the data
```bash
python generate_data.py
```
This creates the merchant, user, ledger, and gateway export datasets.
2. Run payment reconciliation
```bash
python reconcile.py
```
The reconciliation process compares transaction IDs, amounts, and statuses between the internal ledger and gateway export. It creates reports for transactions missing from either source and for amount or status mismatches.
3. Run the dashboard
```bash
python dashboard.py
```
The dashboard calculates key payment metrics and saves charts in the `charts/` folder.
4. Run SQL analysis
Open `paytm_payments.db` in SQLite or DB Browser for SQLite and execute the queries in `sql_queries.sql`.

Key Analyses

The SQL analysis includes chargeback analysis, top merchants by GMV, payment-method analysis, burner-account detection, velocity detection, merchant-wise chargebacks, joins, daily GMV, status summaries, and high-risk transactions.

Dashboard Metrics

Total GMV: Total value of payment transactions.

Success Rate: Percentage of transactions successfully captured.

Chargeback Ratio: Percentage of transactions with chargeback status.

Reconciliation Match Rate: Percentage of transactions that match between the ledger and gateway.

The dashboard also includes daily GMV trends, daily chargeback trends, GMV by payment method, GMV by merchant category, and a top-merchants summary.

Spreadsheet

`merchant_workbook.xlsx` contains merchant and transaction data along with lookup-based analysis. It demonstrates VLOOKUP for merchant information and includes a lookup table for spreadsheet analysis.

Technologies Used

Python, Pandas, NumPy, Matplotlib, SQLite, SQL, and Microsoft Excel.

Notes

The project uses reproducible generated data and transaction IDs as the primary key for reconciliation.
