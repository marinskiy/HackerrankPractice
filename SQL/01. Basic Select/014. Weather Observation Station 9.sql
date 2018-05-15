-- # Problem: https://www.hackerrank.com/challenges/weather-observation-station-9/problem
-- # Score: 10


SELECT DISTINCT CITY
FROM STATION
WHERE REGEXP_LIKE(City, '^[^AEIOU]');
