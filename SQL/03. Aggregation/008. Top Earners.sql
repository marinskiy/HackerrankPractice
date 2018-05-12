-- This is the solution to https://www.hackerrank.com/challenges/earnings-of-employees/problem


SELECT *
FROM (
    SELECT Months * Salary, COUNT(*)
    FROM Employee
    GROUP BY (Months * Salary)
    ORDER BY Months * Salary DESC
    )
WHERE ROWNUM = 1;
