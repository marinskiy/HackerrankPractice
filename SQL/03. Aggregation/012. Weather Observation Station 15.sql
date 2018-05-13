-- # Problem: https://www.hackerrank.com/challenges/weather-observation-station-15/problem
-- # Score: 15


SELECT ROUND(Long_W, 4)
FROM (
    SELECT Long_W
    FROM Station
    WHERE Lat_N < 137.2345
    ORDER BY Lat_N DESC
    )
WHERE ROWNUM = 1;
