# Average check by age group

SELECT age_group, AVG(avg_check) AS avg_group_check FROM
    (
    SELECT n.*, (c.customer_age DIV 10) * 10 AS age_group FROM
        (
        SELECT AVG(transaction_sum) AS avg_check, customer_id FROM Transactions
	        GROUP BY customer_id
        ) AS n
        LEFT JOIN Customers AS c USING (customer_id)
    ) AS m
    GROUP BY age_group
