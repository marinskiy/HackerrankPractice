-- # Problem: https://www.hackerrank.com/challenges/asian-population/problem
-- # Score: 10


SELECT SUM(CITY.POPULATION)
FROM CITY
JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE COUNTRY.CONTINENT = 'Asia';
