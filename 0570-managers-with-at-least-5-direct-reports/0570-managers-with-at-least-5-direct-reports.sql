# Write your MySQL query statement below
select w1.name as name
from Employee w1 
join Employee w2 
on w1.id= w2.managerID 
group by w1.name,w1.id
having count(w2.id)>=5;