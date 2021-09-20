# Favorite merchant type id by age group

WITH age_group_base AS
	(
	SELECT age_group, merchant_type_id, SUM(1) AS trans_n FROM
        (
        SELECT t.*, m.merchant_type_id, (c.customer_age DIV 10) * 10 AS age_group
            FROM Transactions AS t
            LEFT JOIN Merchants AS m USING(merchant_id)
            LEFT JOIN Customers AS c USING(customer_id)
        ) AS n
        GROUP BY age_group, merchant_type_id
	)

SELECT t1.age_group, 
    (SELECT t2.merchant_type_id
    FROM age_group_base AS t2
    WHERE t2.age_group = t1.age_group
    ORDER BY t2.trans_n DESC
    LIMIT 1) AS favorite_merchant_type_id,
    MAX(t1.trans_n) AS trans_n
FROM age_group_base AS t1
GROUP BY t1.age_group    
