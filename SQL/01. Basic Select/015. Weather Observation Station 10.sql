-- # Problem: https://www.hackerrank.com/challenges/weather-observation-station-10/problem
-- # Score: 10


SELECT DISTINCT City
FROM Station
WHERE SUBSTR (CITY, LENGTH(City), 1) NOT IN ('a', 'e', 'i', 'o', 'u');
