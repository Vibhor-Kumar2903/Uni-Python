# pd.merge(df1, df2, on=column_name, how="type_of_join")

import pandas as pd

customer = {
    'Cust_ID' : [1,2,3],
    'Name' : ['Tinku', 'Pinku', 'Rinku']
}

order = {
    'Cust_ID' : [1,2,4],
    'Order_amt' : ['250', '450', '350']
}

df1 = pd.DataFrame(customer)
df2 = pd.DataFrame(order)

print(f"\ncustomer: \n{df1}")
print(f"\norder: \n{df2}")

inner_join_df = pd.merge(df1, df2, on='Cust_ID', how='inner')
print(f"\nInner Join: \n{inner_join_df}")

outer_join_df = pd.merge(df1, df2, on='Cust_ID', how='outer')
print(f"\nOuter Join: \n{outer_join_df}")

left_join_df = pd.merge(df1, df2, on='Cust_ID', how='left')
print(f"\nLeft Join: \n{left_join_df}")

right_join_df = pd.merge(df1, df2, on='Cust_ID', how='right')
print(f"\nRight Join: \n{right_join_df}")


