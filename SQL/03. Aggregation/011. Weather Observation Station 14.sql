-- This is the solution to https://www.hackerrank.com/challenges/weather-observation-station-14/problem


SELECT ROUND(MAX(Lat_N), 4)
FROM Station
WHERE Lat_N < 137.2345;
