-- # Problem: https://www.hackerrank.com/challenges/weather-observation-station-15/problem
-- # Score: 15


select ROUND(LONG_W,4) from STATION where LAT_N=(select max(LAT_N) from STATION where Lat_N < 137.2345);
