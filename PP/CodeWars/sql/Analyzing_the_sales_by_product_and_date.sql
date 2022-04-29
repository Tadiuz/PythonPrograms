
-- https://www.codewars.com/kata/5dac87a0abe9f1001f39e36d/train/sql



-- Task
-- Given the information about sales in a store, calculate the total revenue for each day, month, year, and product.

-- Notes
-- The sales table stores only the dates for which any data has been recorded - the information about individual sales (what was sold, and when) is stored in the sales_details table instead
-- The sales_details table stores totals per product per date
-- Order the result by the product_name, year, month, day columns
-- We're interested only in the product-specific data, so you shouldn't return the total revenue from all sales
-- Input tables
-- ----------------------------------------
-- |    Table      |   Column   |  Type   |
-- |---------------+------------+---------|
-- | products      | id         | int     |
-- |               | name       | text    |
-- |               | price      | numeric |
-- |---------------+------------+---------|
-- | sales         | id         | int     |
-- |               | date       | date    |
-- |---------------+------------+---------|
-- | sales_details | id         | int     |
-- |               | sale_id    | int     |
-- |               | product_id | int     |
-- |               | count      | int     |
-- -----------------------------------------
-- Output table
-- --------------------------
-- |    Column    |  Type   |
-- |--------------+---------|
-- | product_name | text    |
-- | year         | int     |
-- | month        | int     |
-- | day          | int     |
-- | total        | numeric |
-- --------------------------
-- Example output
-- product_name | year | month | day | total
-- -------------+------+-------+-----+------
--  milk        | 2019 | 01    | 01  | 200
--  milk        | 2019 | 01    | 02  | 190
--  milk        | 2019 | 01    |     | 390
--  milk        | 2019 | 02    | 01  | 240
--  milk        | 2019 | 02    |     | 240
--  milk        | 2019 |       |     | 630
--  milk        |      |       |     | 630




SELECT

PR.name as product_name,
DATE_PART('year', S.DATE)::smallint as year,
DATE_PART('month', S.DATE)::smallint as month,
DATE_PART('day', S.DATE)::smallint as day,
SUM((SD.count * PR.price)) as total

FROM products PR
LEFT JOIN sales_details SD
ON SD.product_id = PR.id
LEFT JOIN sales S
ON S.id = SD.sale_id

GROUP BY
PR.name,

ROLLUP (DATE_PART('year', S.DATE), DATE_PART('month', S.DATE), DATE_PART('day', S.DATE))

ORDER BY PR.name, DATE_PART('year', S.DATE), DATE_PART('month', S.DATE), DATE_PART('day', S.DATE)



