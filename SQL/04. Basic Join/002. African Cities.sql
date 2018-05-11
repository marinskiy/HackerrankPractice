-- This is the solution to https://www.hackerrank.com/challenges/african-cities/problem


SELECT CITY.NAME
FROM CITY
JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE CONTINENT = 'Africa';
