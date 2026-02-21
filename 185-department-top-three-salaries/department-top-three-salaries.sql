# Write your MySQL query statement below
SELECT d.name AS Department, e1.name AS Employee, e1.salary AS Salary
FROM Employee e1
JOIN Department d
ON e1.departmentId = d.id
WHERE 3> (
    SELECT count(distinct e2.salary)
    FROM Employee e2
    where e2.salary>e1.salary
    and e1.departmentId = e2.departmentId
);