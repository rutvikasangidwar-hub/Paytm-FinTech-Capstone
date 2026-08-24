Credit Risk & Lending ML
Project Overview
This project applies machine learning and anomaly detection techniques to a simulated lending and transaction dataset. The workflow covers exploratory analysis, preprocessing, credit default prediction, risk-tier analysis, and transaction anomaly detection.
Folder Structure
```text
credit_risk_lending_ml/
├── README.md
├── generate_data.py
├── credit_applicants.csv
├── txn_behaviour.csv
├── credit_risk_model.py
├── anomaly_results.csv
├── bias_awareness_note.md
└── charts/
    ├── 01_default_distribution.png
    ├── 02_bureau_score_missing.png
    ├── 03_feature_distributions.png
    ├── 04_confusion_matrix_logistic.png
    ├── 05_confusion_matrix_tree.png
    ├── 06_roc_comparison.png
    ├── 07_risk_tiers.png
    └── 08_anomaly_detection.png
```
Requirements
```bash
pip install pandas numpy matplotlib scikit-learn
```
Workflow
1. Data Exploration
The applicant dataset is analyzed to understand the default distribution, missing credit bureau scores, and distributions of key financial variables.
2. Feature Engineering
An `is_thin_file` indicator is created to identify applicants with missing credit bureau scores.
3. Train/Test Split
The applicant data is split into training and test sets using a 75/25 stratified split with `random_state=42`.
4. Preprocessing
Numeric missing values are imputed using medians fitted on the training data. Categorical features are encoded where required, and scaling is fitted on training data before being applied to test data.
5. Credit Risk Models
Two models are evaluated:
Logistic Regression
Decision Tree Classifier
Model evaluation includes accuracy, precision, recall, F1 score, confusion matrices, ROC curves, and AUC.
6. Risk Tiers
Logistic Regression predicted probabilities are grouped into four tiers:
Low
Medium
High
Very High
The risk-tier chart shows the observed default rate across these groups.
7. Anomaly Detection
Isolation Forest is applied using:
`txn_hour`
`is_new_device`
`txn_amount_inr`
The analysis uses approximately 15/265 (5.66%) contamination to detect unusual transactions. In the generated results, 15 injected anomalies were present and 11 were detected, giving an anomaly recall of 73.33%.
Charts
Default distribution
Credit bureau score availability
Feature distributions
Logistic Regression confusion matrix
Decision Tree confusion matrix
ROC curve comparison
Risk-tier default rates
Isolation Forest anomaly detection
Bias Awareness
Credit models may produce unfair outcomes when historical data or apparently neutral variables act as proxies for protected characteristics. For this reason, predictive performance should not be the only criterion for model selection. The project includes a separate `bias_awareness_note.md` covering proxy bias, human review, monitoring, documentation, auditability, explainability, and governance.
Technologies Used
Python, Pandas, NumPy, Matplotlib, and Scikit-learn.
