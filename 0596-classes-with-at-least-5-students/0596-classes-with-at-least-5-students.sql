# Write your MySQL query statement below

select class 
from Courses
group by class
having count(student)>=5 # WHERE → individual rows filter karta hai and 
                         # HAVING → GROUP BY ke baad groups filter karta hai
order by class;