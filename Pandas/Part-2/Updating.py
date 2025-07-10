import pandas as pd

data = {
    "Name" : ['Vibhor', 'Ekta', 'Naina', 'Ankit', 'Saurabh', 'Rishu', 'Raj', 'Shivam'],
    "Age" : [10, 20, 30, 12, 15, 18, 13, 17],
    "Salary" : [15000, 20000, 22000, 25000, 16000, 18000, 28000, 30000],
    "Score" : [80, 85, 88, 99, 90, 56, 52, 78]
}

df = pd.DataFrame(data)
print(df)

# df.loc[row_index, 'column_name'] = new_value
df.loc[0, 'Salary'] = 21000
print(f"\n {df}")

#update existing column values
df['Salary'] = df['Salary']* 1.5
print(f"\n {df}")