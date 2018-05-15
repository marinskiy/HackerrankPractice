-- # Problem: https://www.hackerrank.com/challenges/weather-observation-station-11/problem
-- # Score: 15


SELECT DISTINCT City FROM Station
WHERE REGEXP_LIKE(City, '^[^AEIOU]|[^aeiou]$');
