-- # Problem: https://www.hackerrank.com/challenges/revising-the-select-query/problem
-- # Score: 10


SELECT *
FROM CITY
WHERE
    COUNTRYCODE = 'USA'
    AND POPULATION > 100000;
