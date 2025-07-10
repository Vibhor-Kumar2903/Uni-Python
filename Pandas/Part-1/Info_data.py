import pandas as pd

df = pd.read_csv("employees_1.csv")

print(f"Data structure of table : \n")
print(df.info())