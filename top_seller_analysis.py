import pandas as pd
import matplotlib.pyplot as plt
order_items=pd.read_csv("data/olist_order_items_dataset.csv")
print(order_items.head())

top_seller=order_items.groupby("seller_id")["price"].sum().sort_values(ascending=False).head(10)
print(top_seller)
top_seller.plot(kind="bar")
plt.title("Top 10 Sellers")
plt.xlabel("Seller ID")
plt.ylabel("Revenue")
plt.show()