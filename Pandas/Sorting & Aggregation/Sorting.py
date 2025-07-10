"""
1. Sorting data by 1 column using method sort_value()
2. df.sort_value(by="column_Name", True/False, inplace=True)
3. Sorting data by 1 column using || df.sort_value(by=["column_1", "column_2"], ascending=[True, False], inplace=True)
"""

import pandas as pd

data = {
    "Name" : ['Arun', 'Vibhor', 'Ekta', 'Naina', 'Laddu', 'Bittu'],
    "Age" : [25, 30, 26, 24, 2, 11],
    "Salary" : [10000, 25000, 10000, 10500, 5, 500]
    }

df = pd.DataFrame(data)
print("---- Before Sorting ----")
print(f"\n {df}")

# df.sort_values(by="Age", ascending=True, inplace=True)
# print("---- After Sorting by single column ----")
# print(f"\n {df}")

df.sort_values(by=["Name"], ascending=[True], inplace=True)
print("---- After Sorting by multiple column ----")
print(f"\n {df}")

