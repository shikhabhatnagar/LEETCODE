# Write
select e.name from Employee e
join Employee sub 
on e.id= sub.managerId
group by e.id, e.name
having count(sub.id)>=5;