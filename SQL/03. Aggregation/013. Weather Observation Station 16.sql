-- This is the solution to https://www.hackerrank.com/challenges/weather-observation-station-16/problem


SELECT ROUND(MIN(Lat_N), 4)
FROM Station
WHERE Lat_N > 38.7780;
