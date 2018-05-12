-- This is the solution to https://www.hackerrank.com/challenges/the-blunder/problem


SELECT CEIL(AVG(Salary) - AVG(REPLACE(Salary, '0', '')))
FROM EMPLOYEES;
