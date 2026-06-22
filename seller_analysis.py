import pandas as pd
seller=pd.read_csv("data/olist_sellers_dataset.csv")
print(seller.head())
print(seller.info())

#seller_city=seller["seller_city"].value_counts()
#print(seller_city)

#seller_state=seller["seller_state"].value_counts()
#print(seller_state)

#seller_id_counts=seller["seller_id"].nunique()
#print(seller_id_counts)
unique_seller_cities = seller["seller_city"].nunique()

print(unique_seller_cities)