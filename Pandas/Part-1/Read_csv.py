import pandas as pd

df = pd.read_csv("employees_1.csv")
#df = pd.read_csv("employees_1.csv", encoding="utf-8")
#df = pd.read_csv("employees_1.csv", encoding="latin1")

print(df)