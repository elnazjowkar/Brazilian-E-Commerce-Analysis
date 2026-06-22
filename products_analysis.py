import pandas as pd
products=pd.read_csv("data/olist_products_dataset.csv")
#print(products.head())
#print(products.info())

#product_name=products["product_category_name"].value_counts()
#print(product_name)

#unique_categories = products["product_category_name"].nunique()

#print(unique_categories)

#product_length=products["product_description_lenght"].mean()
#print(product_length)
#avg_product_photo=products["product_photos_qty"].mean()
#print(avg_product_photo)

#max_weight = products["product_weight_g"].max()

#print(max_weight)
min_weight = products["product_weight_g"].min()

print(min_weight)