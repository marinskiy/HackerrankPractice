-- # Problem: https://www.hackerrank.com/challenges/the-report/problem
-- # Score: 20


SELECT
    CASE WHEN G.Grade > 7 THEN S.Name ELSE 'NULL' END AS NameOrNull
    , G.Grade
    , S.Marks
FROM Students S
JOIN Grades G ON S.Marks BETWEEN G.Min_Mark AND G.Max_Mark
ORDER BY G.Grade DESC, NameOrNull ASC, S.Marks ASC;
