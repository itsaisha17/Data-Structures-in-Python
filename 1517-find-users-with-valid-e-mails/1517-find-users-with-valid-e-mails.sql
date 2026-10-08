#REGULAR EXPRESSION

select * from
Users
where REGEXP_LIKE( 
    mail,'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com$','c'
)

#USED BINARY AS ITS CASE SENSTIVE
