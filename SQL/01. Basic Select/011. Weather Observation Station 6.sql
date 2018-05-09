-- This is the solution to https://www.hackerrank.com/challenges/weather-observation-station-6/problem


SELECT DISTINCT CITY
FROM STATION
WHERE SUBSTR (CITY, 1, 1) IN ('A', 'E', 'I', 'O', 'U');
