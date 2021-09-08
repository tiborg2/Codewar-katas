WITH special_sales AS 
  (
    SELECT * 
    FROM sales 
    WHERE price > 90.00
  )
SELECT * 
FROM department
WHERE department_id IN (SELECT department_id
             FROM special_sales)