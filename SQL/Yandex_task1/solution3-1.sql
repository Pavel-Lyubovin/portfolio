# Average transactions in year by customers in age groups

SELECT age_group, AVG(year_trans_n) AS avg_year_trans_n FROM
    ( 
    SELECT m.*, (c.customer_age DIV 10) * 10 AS age_group FROM
        (
        SELECT SUM(1) AS year_trans_n, customer_id, year FROM 
	        (
	        SELECT *, YEAR(transaction_dttm) AS year FROM Transactions
            ) AS n
            GROUP BY customer_id, year 
        ) AS m
        LEFT JOIN Customers AS c USING (customer_id)
    ) as k
    GROUP BY age_group 
