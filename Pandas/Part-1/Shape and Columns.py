import pandas as pd

data = {
    "name" : ['Vibhor', 'Ekta', 'Naina', 'Ankit', 'Saurabh', 'Rishu', 'Raj', 'Shivam'],
    "Age":[10, 20, 30, 12, 15, 18, 13, 17],
    "Salary": [15000, 20000, 22000, 25000, 16000, 18000, 28000, 30000],
    "Score": [80, 85, 88, 99, 90, 56, 52, 78]
}

df = pd.DataFrame(data)

print(f"\nTable : \n{df}")
print(f"\n Columns : {df.columns}")
print(f"\n Shape : {df.shape}")


