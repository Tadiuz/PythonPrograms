-- https://www.codewars.com/kata/59be9f425227ddd60c00003b/train/sql

-- Write a SELECT query which will return all prime numbers smaller than 100 in ascending order.

-- Your query should return one column named prime.


SELECT  number  as prime

FROM generate_series(2,100) t1(number)

WHERE NOT EXISTS(
  SELECT * 
  FROM generate_series(2, t1.number-1) as t2(number2)
  WHERE t1.number % t2.number2 = 0

)