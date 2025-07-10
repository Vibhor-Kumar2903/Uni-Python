import pandas as pd

region_1 = {
    'Cust_ID' : [1,2],
    'Name' : ['Gopal', 'Raju']
}

region_2 = {
    'Cust_ID' : [3,4],
    'Name' : ['Shyam', 'Babu Rao']
}

df_region_1 = pd.DataFrame(region_1)
df_region_2 = pd.DataFrame(region_2)

vertical_df_concat = pd.concat([df_region_1, df_region_2], axis=0, ignore_index=True)
print(f"\nVertical Concatenation : \n{vertical_df_concat}")

horizontal_df_concat = pd.concat([df_region_1, df_region_2], axis=1, ignore_index=True)
print(f"\nHorizontal Concatenation : \n{horizontal_df_concat}")