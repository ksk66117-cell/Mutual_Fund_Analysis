-- Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV
SELECT AVG(nav) AS average_nav
FROM fact_nav;

-- SIP transactions count
SELECT COUNT(*) AS sip_count
FROM fact_transactions
WHERE transaction_type = 'SIP';

-- Transactions by state
SELECT state, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state;

-- Verified KYC count
SELECT kyc_status, COUNT(*)
FROM fact_transactions
GROUP BY kyc_status;

-- Average expense ratio
SELECT AVG(expense_ratio_pct)
FROM fact_performance;

-- Funds with expense ratio below 1%
SELECT scheme_name
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- Average 1-year return
SELECT AVG(return_1yr_pct)
FROM fact_performance;

-- Risk grade count
SELECT risk_grade, COUNT(*)
FROM fact_performance
GROUP BY risk_grade;

-- Average alpha
SELECT AVG(alpha)