import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

data = {
    "Name" : ['Vibhor', None, 'Naina', 'Ankit', 'Saurabh', 'Rishu', 'Raj', 'Shivam'],
    "Age" : [10, None, 30, 12, 15, 18, 13, 17],
    "Salary" : [15000, None, 22000, 25000, 16000, 18000, 28000, 30000],
    "Score" : [80, None, 88, 99, 90, 56, 52, 78]
}

df = pd.DataFrame(data)
print(f"\n {df}")

"""
1. Interpolation use to replace the null data from calculating the estimate of existing data.
2. It preserve data integrity 
3. Avoid data loss 
4. Type of interpolation : linear, polynomial, time.
"""

df.interpolate(method='linear', axis=0, inplace=True)
print(f"\n {df}")
