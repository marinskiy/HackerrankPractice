-- # Problem: https://www.hackerrank.com/challenges/the-company/problem
-- # Score: 30


SELECT
    c.company_code,
    c.founder,
    COUNT(DISTINCT(lm.lead_manager_code)),
    COUNT(DISTINCT(sm.senior_manager_code)),
    COUNT(DISTINCT(m.manager_code)),
    COUNT(DISTINCT(e.employee_code))
FROM Company c, Lead_Manager lm, Senior_Manager sm, Manager m, Employee e
WHERE c.company_code = lm.company_code AND c.company_code = sm.company_code AND c.company_code = m.company_code AND c.company_code = e.company_code
GROUP BY c.company_code, c.founder ORDER BY c.company_code;
