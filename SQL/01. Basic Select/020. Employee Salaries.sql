-- # Problem: https://www.hackerrank.com/challenges/salary-of-employees/problem
-- # Score: 10


SELECT Name
FROM Employee
WHERE Months < 10 AND Salary > 2000;
