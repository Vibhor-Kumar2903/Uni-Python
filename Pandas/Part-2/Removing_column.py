import pandas as pd
import time
data = {
    "Name" : ['Vibhor', 'Ekta', 'Naina', 'Ankit', 'Saurabh', 'Rishu', 'Raj', 'Shivam'],
    "Age" : [10, 20, 30, 12, 15, 18, 13, 17],
    "Salary" : [15000, 20000, 22000, 25000, 16000, 18000, 28000, 30000],
    "Score" : [80, 85, 88, 99, 90, 56, 52, 78]
}

df = pd.DataFrame(data)
print(df)

df.insert(0, "Emp_Id", [1,2,3,4,5,6,7,8])
print(f"\n {df}")

time.sleep(5)
# df.drop(column = ["column_name"], inplace=True)
df.drop(columns=['Emp_Id'], inplace=True)
print(f"\n {df}")

time.sleep(5)
# drop multiple columns
df.drop(columns=['Score', 'Age'], inplace=True)
print(f"\n {df}")
