-- This is the solution to https://www.hackerrank.com/challenges/weather-observation-station-2/problem


SELECT ROUND(SUM(Lat_N), 2), ROUND(SUM(Long_W), 2)
FROM Station;
