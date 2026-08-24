-- ============================================
-- Paytm Payments & Fraud Analytics
-- SQL Queries
-- ============================================

-- 1. Total Chargeback Analysis
SELECT
    COUNT(*) AS chargeback_transactions,
    COUNT(DISTINCT user_id) AS unique_users,
    SUM(amount_inr) AS total_chargeback_amount
FROM transactions
WHERE status = 'chargeback';

-- 2. Top 10 Merchants by GMV
SELECT
    m.merchant_name,
    SUM(t.amount_inr) AS total_gmv
FROM transactions t
INNER JOIN merchants m
ON t.merchant_id = m.merchant_id
GROUP BY m.merchant_name
ORDER BY total_gmv DESC
LIMIT 10;

-- 3. Transaction Count by Payment Method
SELECT payment_method,
COUNT(*) AS transaction_count,
SUM(amount_inr) AS total_amount
FROM transactions
GROUP BY payment_method
ORDER BY total_amount DESC;

-- 4. Burner Account Detection
SELECT
t.transaction_id,
t.user_id,
u.signup_date,
t.transaction_time,
t.amount_inr,
t.status
FROM transactions t
JOIN users u
ON t.user_id=u.user_id
WHERE t.status='chargeback'
AND julianday(t.transaction_time)-julianday(u.signup_date)>=0
AND julianday(t.transaction_time)-julianday(u.signup_date)<30;

-- 5. Velocity Attack Detection
SELECT
user_id,
strftime('%Y-%m-%d %H:', transaction_time) ||
printf('%02d',(CAST(strftime('%M',transaction_time) AS INTEGER)/10)*10)
AS ten_min_bucket,
COUNT(*) AS txn_count
FROM transactions
GROUP BY user_id, ten_min_bucket
HAVING COUNT(*)>=3
ORDER BY txn_count DESC;

-- 6. Merchant-wise Chargebacks
SELECT
m.merchant_name,
COUNT(*) AS chargebacks,
SUM(t.amount_inr) AS total_chargeback_amount
FROM transactions t
INNER JOIN merchants m
ON t.merchant_id=m.merchant_id
WHERE t.status='chargeback'
GROUP BY m.merchant_name
ORDER BY chargebacks DESC;

-- 7. LEFT JOIN Example
SELECT
m.merchant_name,
COUNT(t.transaction_id) AS total_transactions
FROM merchants m
LEFT JOIN transactions t
ON m.merchant_id=t.merchant_id
GROUP BY m.merchant_name;

-- 8. Daily GMV
SELECT DATE(transaction_time) AS txn_date,
SUM(amount_inr) AS daily_gmv
FROM transactions
GROUP BY DATE(transaction_time)
ORDER BY txn_date;

-- 9. Status-wise Transactions
SELECT status,
COUNT(*) AS total_transactions,
SUM(amount_inr) AS total_amount
FROM transactions
GROUP BY status;

-- 10. Top 5 High Risk Transactions
SELECT
transaction_id,
user_id,
merchant_id,
amount_inr,
risk_score
FROM transactions
ORDER BY risk_score DESC
LIMIT 5;
