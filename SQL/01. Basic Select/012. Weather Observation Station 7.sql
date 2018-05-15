-- # Problem: https://www.hackerrank.com/challenges/weather-observation-station-7/problem
-- # Score: 10


SELECT DISTINCT CITY
FROM STATION
WHERE REGEXP_LIKE(City, '[aeiou]$');
