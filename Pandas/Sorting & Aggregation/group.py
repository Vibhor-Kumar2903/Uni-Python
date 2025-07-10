import pandas as pd
from Tools.scripts.verify_ensurepip_wheels import print_notice

data = {
    "Name" : ['Vibhor', 'Ekta', 'Naina', 'Laddu', 'Bittu'],
    "Age" : [30, 24, 24, 21, 21],
    "Salary" : [25000, 10000, 10500, 5000, 5500]
    }

df = pd.DataFrame(data)
print(f"\n {df}")

# grouped_data_1 = df.groupby("Age")["Salary"].sum()
# print(f"\nGrouped_data \n{grouped_data_1}")

grouped_data_2 = df.groupby(["Age", "Name"])["Salary"].sum()
print(f"\nGrouped_data \n{grouped_data_2}")

"""
Aggregation :
1. sum()
2. count()
3. mean()
4. max()
5. min()
"""

