# Write your MySQL query statement below

select id, count(id) as num 
from (
select requester_id as id 
from RequestAccepted
union all                    #union-> distinct leta hai & union all->sare
select accepter_id as id 
from RequestAccepted
) temp                 #alias
group by id
order by num desc
limit 1;
