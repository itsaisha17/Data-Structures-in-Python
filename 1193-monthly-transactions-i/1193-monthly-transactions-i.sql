#month-> date_format(trans_date,'%y-%m')as month
#country-> in table
#trans_count->count(*) as trans_count,
#approved_count->table
#trans_total_amount->
#approved_total_amount-> table

select date_format(trans_date,'%Y-%m')
as month,
country ,
count(*) as trans_count,
count(case when state='approved' then 1 end) as approved_count,
sum(amount) as trans_total_amount,
sum(case when state='approved'then amount else 0 end) as approved_total_amount
from Transactions
group by month,
country;

