import  pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/olist_order_items_dataset.csv")
print(df.head())
print(df.info())
df["shipping_limit_date"]=pd.to_datetime(df["shipping_limit_date"])
print(df.info())
df["month"]=df["shipping_limit_date"].dt.month
df["year"]=df["shipping_limit_date"].dt.year
monthly_sales = df.groupby("month")["price"].sum()
print(monthly_sales)
#monthly_sales.plot(kind="bar")
#plt.title("monthly_sales")
#plt.xlabel("month")
#plt.ylabel("Revenue")
#plt.show()

yearly_sales=df.groupby("year")["price"].sum()
print(yearly_sales)
#yearly_sales.plot(kind="bar")
#plt.title("yearly_sales")
#plt.xlabel("year")
#plt.ylabel("Revenue")
#plt.show()
orders=pd.read_csv("data/olist_orders_dataset.csv")
orders.head()
print(orders.info())

orders["order_purchase_timestamp"]=pd.to_datetime(orders["order_purchase_timestamp"])
print(orders.info())
orders["order_status"].value_counts()
print(orders["order_status"].value_counts())
orders["order_delivered_customer_date"]=pd.to_datetime(orders["order_delivered_customer_date"])
print(orders["order_delivered_customer_date"])

orders["delivery_time"]=(orders["order_delivered_customer_date"]-orders["order_purchase_timestamp"]).dt.days

#print(orders["delivery_time"])
print(orders["delivery_time"].mean())

orders["month"] = orders["order_purchase_timestamp"].dt.month
monthly_orders=orders.groupby("month")["order_id"].count()
print(monthly_orders)
print(monthly_orders.sort_values(ascending=False))
#monthly_orders.plot(kind="bar")
#plt.title("monthly_orders")
#plt.xlabel("month")
#plt.ylabel("Number of orders")
#plt.show()

orders["order_delivered_customer_date"]=pd.to_datetime(orders["order_delivered_customer_date"])
orders["order_estimated_delivery_date"]=pd.to_datetime(orders["order_estimated_delivery_date"])
print(orders.info())
late_orders=orders[orders["order_delivered_customer_date"]>orders["order_estimated_delivery_date"]]
print(late_orders.shape[0])


late_percentage = (late_orders.shape[0] / orders.shape[0]) * 100
print(late_percentage)
monthly_late_orders=late_orders.groupby("month")["order_id"].count()
print(monthly_late_orders)

monthly_late_orders = late_orders.groupby("month")["order_id"].count()
print(monthly_late_orders)

print(monthly_late_orders.sort_values(ascending=False))