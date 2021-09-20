# Top 3 regions by customer expenses in the current year

SELECT m.merchant_region, sum(t.transaction_sum) AS region_sum FROM Transactions AS t 
    LEFT JOIN Merchants AS m USING(merchant_id)
    WHERE YEAR(transaction_dttm) = YEAR(NOW())
    GROUP BY merchant_region
    ORDER BY region_sum DESC LIMIT 3
