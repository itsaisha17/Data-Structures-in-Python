# Write your MySQL query statement below

Delete p1
from Person p1
inner join person p2
on p1.email=p2.email
and p1.id > p2.id 