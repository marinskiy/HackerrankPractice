-- This is the solution to https://www.hackerrank.com/challenges/japan-population/problem


SELECT SUM(Population)
FROM City
WHERE CountryCode = 'JPN';
