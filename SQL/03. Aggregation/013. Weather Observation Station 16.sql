-- # Problem: https://www.hackerrank.com/challenges/weather-observation-station-16/problem
-- # Score: 10


SELECT ROUND(MIN(Lat_N), 4)
FROM Station
WHERE Lat_N > 38.7780;
