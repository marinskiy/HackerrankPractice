-- # Problem: https://www.hackerrank.com/challenges/japan-population/problem
-- # Score: 10


SELECT SUM(Population)
FROM City
WHERE CountryCode = 'JPN';
