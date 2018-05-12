-- This is the solution to https://www.hackerrank.com/challenges/weather-observation-station-13/problem


SELECT ROUND(SUM(Lat_N), 4)
FROM STATION
WHERE Lat_N BETWEEN 38.7880 AND 137.2345;
