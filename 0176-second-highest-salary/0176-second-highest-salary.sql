select (
    select distinct salary
    from Employee
    order by salary desc
    limit 1 OFFSET 1

) as SecondHighestSalary;

#offset-> skipss the number
#since we wanted second highest it skipped the first one