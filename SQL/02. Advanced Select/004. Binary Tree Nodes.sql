-- # Problem: https://www.hackerrank.com/challenges/binary-search-tree-1/problem
-- # Score: 30


SELECT N,
    CASE
        WHEN P IS NULL THEN 'Root'
        WHEN N IN (SELECT P FROM BST) THEN 'Inner'
        ELSE 'Leaf'
    END
FROM BST
ORDER BY N;
