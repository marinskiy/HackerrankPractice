-- # Problem: https://www.hackerrank.com/challenges/more-than-75-marks/problem
-- # Score: 15


SELECT Name
FROM Students
WHERE Marks > 75
ORDER BY SUBSTR(Name, - 3), Id ASC;
