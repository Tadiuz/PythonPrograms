-- https://www.codewars.com/kata/59821d485a49f4d71f00000b/train/sql

-- Yes it's Fibonacci yet again ! But this time it's SQL.

-- You need to create a select statement which will produce first 90 Fibonnacci numbers. The column name is - number

-- Fibbonaccii sequence is:

--  0, 1, 1, 2, 3, 5, 8, 13, ..., 89, 144, 233, 377, ...
-- where

-- f(0) = 0
-- f(1) = 1
-- ...
-- f(n) = f(n-1) + f(n-2)
-- Have fun!


WITH RECURSIVE fibonacci(first, second, step) AS (
    SELECT 0::bigint as first, 1::bigint as second, 1::bigint as step
  UNION ALL
    SELECT second, first+second, step+1
    FROM fibonacci f
    WHERE f.step < 90
)
SELECT first as number
FROM fibonacci