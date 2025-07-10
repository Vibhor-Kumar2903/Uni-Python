import pandas as pd

data = {
    "Name" : ['vibhor', 'ekta', 'naina', 'ankit', 'Saurabh', 'Rishu', 'Raj', 'Shivam'],
    "Age":[10, 20, 30, 12, 15, 18, 13, 17],
    "Salary": [15000, 20000, 22000, 25000, 16000, 18000, 28000, 30000],
    "Score": [80, 85, 88, 99, 90, 56, 52, 78]
}

df = pd.DataFrame(data)

print(f"\nSample DataFrame : \n{df}")

print(f"\nAll column in sample data : \n{df.columns}")

print(f"\nSample data single column : \n{df['Name']}")

print(f"\nSample data multiple columns (via passing colums): \n{df[['Name', 'Age']]}" )
#OR
subset_of_sample_data = ['Name', 'Age']
print(f"\nSample data multiple columns (via passing variable): \n{df[subset_of_sample_data]}" )

#High Salary (filter row data)
filter_row = df[df['Salary'] > 25000] ##will return dataframe
#filter_row = df['Salary'] > 25000   ##Will return boolean
print(f"\nHighly paid employees : \n{filter_row}")


#Filter row with multiple condition
filter_row_1 = df[(df['Salary']>25000) & (df['Salary']<30000)]
print(f"\nHighly paid employees : \n{filter_row_1}")


#Filter row with multiple condition
filter_row_2 = df[(df['Salary']>20000) | (df['Age']<12)]
print(f"\nHighly paid employees : \n{filter_row_2}")

