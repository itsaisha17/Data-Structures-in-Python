Select  
ROUND(AVG(order_date= customer_pref_delivery_date)*100,2) #to calc the percentage
as immediate_percentage
from Delivery
where (customer_id,order_date) IN (        #this query we run for comp which big
    select customer_id, min(order_date)
    from Delivery
    group by customer_id
)