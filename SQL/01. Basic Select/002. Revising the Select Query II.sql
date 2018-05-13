-- # Problem: https://www.hackerrank.com/challenges/revising-the-select-query-2/problem
-- # Score: 10


SELECT NAME
FROM CITY
WHERE
    COUNTRYCODE = 'USA'
    AND POPULATION > 120000;
