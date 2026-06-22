import pandas as pd
customers=pd.read_csv("data/olist_customers_dataset.csv")
#print(customers.head())
#print(customers.info())

#city_counts = customers["customer_city"].value_counts()

#print(city_counts)
#state_counts = customers["customer_state"].value_counts()

#print(state_counts)

unique_customer=customers["customer_unique_id"].nunique()
print(unique_customer)