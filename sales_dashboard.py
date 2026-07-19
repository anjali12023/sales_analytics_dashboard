import pandas as pd

order = pd.read_csv("orders.csv")
#parsing dates as dt objects
order["order_date"] = pd.to_datetime(order["order_date"])


# print(order["product_id"].to_string())
#calculating revenue: 
#product id
#group by order_id
#see product id + cost associated with it 
#check order is not withdrawn/ cancelled

completed = order[(order["order_status"] == "Completed")]
# print(completed)
#sort orders by month:
order["month"] = order.order_date.dt.to_period("M")
monthly_revenue = order.groupby("month")["total_amount"].sum()
print(monthly_revenue)