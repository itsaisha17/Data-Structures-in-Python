##-> WINDOW FUNCTION
select DISTINCT num as ConsecutiveNums
from (
    select num,
        lead(num,1) over (order by id) as num_1,
        lead(num,2) over (order by id)as num_2   
        from Logs
)x
where num=num_1
    and num=num_2
    ;