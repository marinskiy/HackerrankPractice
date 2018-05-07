-- This is the solution to https://www.hackerrank.com/challenges/weather-observation-station-1/problem


SELECT DISTINCT CITY
FROM STATION
WHERE MOD(ID, 2) = 0;
