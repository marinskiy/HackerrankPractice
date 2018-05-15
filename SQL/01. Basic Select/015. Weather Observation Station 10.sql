-- # Problem: https://www.hackerrank.com/challenges/weather-observation-station-10/problem
-- # Score: 10


SELECT DISTINCT City
FROM Station
WHERE REGEXP_LIKE(City, '[^aeiou]$');
