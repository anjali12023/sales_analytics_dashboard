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
# print(group["customer_id"].count().idxmax())
#join both tables together 

best_customers = (order.groupby("customer_id")["total_amount"].sum()
                   .sort_values(ascending=False)
                   .to_frame().merge(customers, on="customer_id"))
# print(best_customers.to_string())

#PROFIT MARGINS:
#profit = revenue - cost
order["profit"] = order["total_amount"] - (order["unit_cost"]*order["quantity"])
order["margin_pct"] = order["profit"] / order["total_amount"]
# print(order)

#SALES BY STATE: 
#number of orders: 
state = order.groupby("ship_state")["total_amount"].sum().sort_values(ascending=False)
# print(state)

#MONTHLY GROWTH
monthly_growth = monthly_revenue.pct_change()
# print(monthly_growth)

##########################################################
#DATA CLEANING

#delete duplicate rows:
order = order.drop_duplicates()

#remove rows with quantiity = 0
orders_clean = order[(order["quantity"] != 0)]

#Handle missing data
order["discount_pct"] = order["discount_pct"].replace({0.00: "-"})

#Removed Returned + Cancelled orders to help with revenue calculating
order = order[(order["order_status"] != "Returned")]
order = order[(order["order_status"] != "Cancelled")]

print(order.to_string())