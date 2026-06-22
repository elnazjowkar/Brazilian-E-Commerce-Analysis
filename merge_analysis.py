import pandas as pd
import matplotlib.pyplot as plt


products = pd.read_csv("data/olist_products_dataset.csv")

order_items = pd.read_csv("data/olist_order_items_dataset.csv")
merged = order_items.merge(
    products,
    on="product_id"
)
print(merged.head())
popular_category = merged["product_category_name"].value_counts()

print(popular_category)

category_revenue = merged.groupby(
    "product_category_name"
)["price"].sum()
print(category_revenue)
print(category_revenue.sort_values(ascending=False))

top_products = order_items["product_id"].value_counts()

print(top_products)

category_revenue = merged.groupby(
    "product_category_name"
)["price"].sum().sort_values(
    ascending=False
).head(10)

category_revenue.plot(kind="bar")

plt.title("Top 10 Categories by Revenue")
plt.xlabel("Category")
plt.ylabel("Revenue")

plt.show()