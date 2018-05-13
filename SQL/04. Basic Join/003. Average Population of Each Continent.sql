-- # Problem: https://www.hackerrank.com/challenges/average-population-of-each-continent/problem
-- # Score: 10


SELECT COUNTRY.CONTINENT, FLOOR(AVG(CITY.POPULATION))
FROM CITY
JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
GROUP BY COUNTRY.CONTINENT;
