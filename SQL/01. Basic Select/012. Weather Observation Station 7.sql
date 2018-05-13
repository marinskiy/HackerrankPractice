-- # Problem: https://www.hackerrank.com/challenges/weather-observation-station-7/problem
-- # Score: 10


SELECT DISTINCT CITY
FROM STATION
WHERE SUBSTR (CITY, LENGTH(CITY), 1) IN ('a', 'e', 'i', 'o', 'u');
