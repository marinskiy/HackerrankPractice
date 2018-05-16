-- # Problem: https://www.hackerrank.com/challenges/salary-of-employees/problem
-- # Score: 10


SELECT Name
FROM Employee
WHERE Salary > 2000 AND Months < 10
ORDER BY Employee_id;
