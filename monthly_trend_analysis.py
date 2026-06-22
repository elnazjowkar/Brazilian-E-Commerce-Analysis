import pandas as pd
import matplotlib.pyplot as plt
order_items=pd.read_csv("data/olist_order_items_dataset.csv")
print(order_items.head())
orders=pd.read_csv("data/olist_orders_dataset.csv")
print(orders.head())
orders["order_purchase_timestamp"]=pd.to_datetime(orders["order_purchase_timestamp"])
orders["month"]=orders["order_purchase_timestamp"].dt.month
print(orders.head)
merged=order_items.merge(orders, on ="order_id")
monthly_sales=merged.groupby("month")["price"].sum()
print(monthly_sales)
monthly_sales.plot(kind="bar")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()
