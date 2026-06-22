import pandas as pd

products = pd.read_csv("data/olist_products_dataset.csv")

order_items = pd.read_csv("data/olist_order_items_dataset.csv")

payments = pd.read_csv("data/olist_order_payments_dataset.csv")
merged_1 = order_items.merge(
    products,
    on="product_id"
)
final_merged = merged_1.merge(
    payments,
    on="order_id"
)
print(final_merged.head())
category_payment = final_merged.groupby(
    ["product_category_name", "payment_type"]
).size()

print(category_payment)
category_payment = final_merged.groupby(
    ["product_category_name", "payment_type"]
).size().sort_values(ascending=False)

print(category_payment)