import pandas as pd

data = {
    "Name" : ['Arun', 'Vibhor', 'Ekta', 'Naina', 'Laddu', 'Bittu'],
    "Age" : [25, 30, 26, 24, 2, 11],
    "Salary" : [10000, 25000, 10000, 10500, 5, 500]
    }

df = pd.DataFrame(data)
print(f"\n {df}")

avg_sal = df['Salary'].mean()
avg_sal = avg_sal.round()

print(f"\nAverage salary = {avg_sal}")
