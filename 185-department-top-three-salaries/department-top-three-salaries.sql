# Write your MySQL query statement below
select d.name as Department,
e.name as employee,
e.salary as Salary
from 
(
    select *,
    dense_Rank() over(
        partition by departmentId 
        order by salary Desc
    ) as rnk
  from Employee
) e
join Department d
on e.departmentId = d.id 
where rnk <=3;