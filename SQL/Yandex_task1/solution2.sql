# Top 3 merchant_type_id by average check

SELECT m.merchant_type_id, AVG(t.transaction_sum) AS avg_check FROM Transactions AS t
    LEFT JOIN Merchants AS m USING(merchant_id)
    GROUP BY merchant_type_id
    ORDER BY avg_check DESC LIMIT 3
