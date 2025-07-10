import pandas as pd

linear_data = {
    'time' : [1,2,3,4,5,6],
    'value' : [10,None,20,None,30,None]
}

df = pd.DataFrame(linear_data)
print(f"\n {df}")

df['value'] = df['value'].interpolate(method='linear')
print(f"\n {df}")

"""
1. Interpolation will not work on categorical data.
"""