import pandas as pd 
payments=pd.read_csv("data/olist_order_payments_dataset.csv")
#print(payments.head())
#print(payments.info())

#payment_types = payments["payment_type"].value_counts()
#print(payment_types)
#average_payment=payments["payment_value"].mean()
#print(average_payment)

#installments_count=payments["payment_installments"].value_counts().sort_index()
#print(installments_count)

max_payment=payments["payment_value"].max()
print(max_payment)
min_payment=payments["payment_value"].min()
print(min_payment)