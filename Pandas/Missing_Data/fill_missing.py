import pandas as pd

data = {
    "Name" : ['Vibhor', None, 'Naina', 'Ankit', 'Saurabh', 'Rishu', 'Raj', 'Shivam'],
    "Age" : [10, None, 30, 12, 15, 18, 13, 17],
    "Salary" : [15000, None, 22000, 25000, 16000, 18000, 28000, 30000],
    "Score" : [80, None, 88, 99, 90, 56, 52, 78]
}

df = pd.DataFrame(data)
print(f"\n {df}")

# df['Age'].fillna(df['Age'].mean(), inplace=True)
# try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead,
# to perform the operation inplace on the original object.
df['Age'] = df['Age'].mean()
print(f"\n {df}")
