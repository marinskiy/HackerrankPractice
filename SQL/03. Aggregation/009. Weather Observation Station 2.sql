-- # Problem: https://www.hackerrank.com/challenges/weather-observation-station-2/problem
-- # Score: 15


SELECT ROUND(SUM(Lat_N), 2), ROUND(SUM(Long_W), 2)
FROM Station;
