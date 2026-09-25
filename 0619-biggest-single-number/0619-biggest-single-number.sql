select max(num) as num
from (                         #t--> is temp alias always after from as result table
    select num from MyNumbers
    group by num
    having count(*)=1
    
    ) t;