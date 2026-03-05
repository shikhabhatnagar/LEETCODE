# Write your MySQL query statement below
select d.name as Department,
e.name as Employee,
e.salary as Salary
from employee e join Department d
on e.departmentID=d.id
where(e.departmentId,e.salary) in
( select 
departmentId,
max(salary)
from Employee
group by DepartmentId
)