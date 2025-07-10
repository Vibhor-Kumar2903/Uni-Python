import pandas as pd

data = {
    "Name" : ['Vibhor', 'Ekta', 'Naina', 'Ankit', 'Saurabh', 'Rishu', 'Raj', 'Shivam'],
    "Age":[10, 20, 30, 12, 15, 18, 13, 17],
    "Salary": [15000, 20000, 22000, 25000, 16000, 18000, 28000, 30000],
    "Score": [80, 85, 88, 99, 90, 56, 52, 78]
}

df = pd.DataFrame(data)
print(df)

#Direct assignment method.
df['Bonus'] = df['Salary'] * 0.1
print(df)

# Insert Method
# df.insert(column_location, column_name, values or data)
df.insert(0, 'Emp ID', [1,2,3,4,5,6,7,8])
print(df)


