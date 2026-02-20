# Write your MySQL query statement below
select email from person 
group by Email having count(*)>1