import pandas as pd

df = pd.read_csv("employees_1.csv")

print(f"\n Rows from start : \n{df.head()}")
print(f"\n Rows from last : \n{df.tail()}")

