-- This is the solution to https://www.hackerrank.com/challenges/revising-the-select-query/problem


SELECT *
FROM CITY
WHERE
    COUNTRYCODE = 'USA'
    AND POPULATION > 100000;
