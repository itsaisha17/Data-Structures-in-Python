#delivery date= order date-> immediate ; else scheduled
#first order-> earliest order date
# %immediate orders in first order 

select 
ROUND(AVG(order_date=customer_pref_delivery_date)*100,2) as immediate_percentage
from Delivery
where (customer_id,order_date) IN(
    select customer_id, min(order_date) 
    from delivery
    group by customer_id
)