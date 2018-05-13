-- # Problem: https://www.hackerrank.com/challenges/weather-observation-station-9/problem
-- # Score: 10


SELECT DISTINCT CITY
FROM STATION
WHERE SUBSTR (CITY, 1, 1) NOT IN ('A', 'E', 'I', 'O', 'U');
