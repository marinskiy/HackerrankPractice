-- # Problem: https://www.hackerrank.com/challenges/african-cities/problem
-- # Score: 10


SELECT CITY.NAME
FROM CITY
JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE CONTINENT = 'Africa';
