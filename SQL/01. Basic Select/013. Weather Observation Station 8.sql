-- # Problem: https://www.hackerrank.com/challenges/weather-observation-station-8/problem
-- # Score: 15


SELECT DISTINCT CITY
FROM STATION
WHERE REGEXP_LIKE(City, '^[AEIOU].*[aeiou]$');
