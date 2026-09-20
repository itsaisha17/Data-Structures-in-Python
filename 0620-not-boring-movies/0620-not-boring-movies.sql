# Write your MySQL query statement below
#0dd-1-3-5-7-9
#not boring
select id,movie,description,rating from Cinema 
where id % 2 !=0 
and
Cinema.description!='boring'
order by rating desc;