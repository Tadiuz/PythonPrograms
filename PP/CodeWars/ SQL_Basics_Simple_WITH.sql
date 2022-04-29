-- https://www.codewars.com/kata/5811501c2d35672d4f000146/train/sql

-- For this challenge you need to create a SELECT statement, this SELECT statement will use an IN to check whether a department has had a sale with a price over 90.00 dollars BUT the sql MUST use the WITH statement which will be used to select all columns from sales where the price is greater than 90.00, you must call this sub-query special_sales.

-- departments table schema
-- id
-- name
-- sales table schema
-- id
-- department_id (department foreign key)
-- name
-- price
-- card_name
-- card_number
-- transaction_date
-- resultant table schema
-- id
-- name
-- NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing.

-- Create your SELECT statement here

WITH special_sales AS (
  SELECT  price FROM sales
  where  price >= 90

)

SELECT 
DISTINCT

dp.id as id,
dp.name


FROM departments  dp
left join sales s
on dp.id = s.department_id
where s.price in (select price from special_sales)

ORDER BY dp.id