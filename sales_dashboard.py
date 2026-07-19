import pandas as pd

order = pd.read_csv("orders.csv")
customers = pd.read_csv("customers.csv")

#parsing dates as dt objects
order["order_date"] = pd.to_datetime(order["order_date"])

#monthly revenue
completed = order[(order["order_status"] == "Completed")]
# print(completed)
#sort orders by month:
order["month"] = order.order_date.dt.to_period("M")
monthly_revenue = order.groupby("month")["total_amount"].sum()
# print(monthly_revenue)

#Top Selling products: 


#Best customers: 
group = order.groupby("customer_id")
#customer with most orders: 
print(group["customer_id"].count().idxmax())
#join both tables together 

best_customers = (order.groupby("customer_id")["total_amount"].sum()
                   .sort_values(ascending=False)
                   .to_frame().merge(customers, on="customer_id"))
print(best_customers.to_string())