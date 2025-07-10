import numpy as np

arr = np.array([1,2,np.nan,3,4,np.nan,5,6])
print(f"\nWith NaN : \n{arr}")

cleaned_1 = np.nan_to_num(arr, nan=10)
print(f"\nNaN is cleared : \n{cleaned_1}")




arr = np.array([1,2,np.nan,3,4,np.nan,5,6])
print(f"\nWith NaN : \n{arr}")

cleaned_2 = np.nan_to_num(arr)
print(f"\nNaN is cleared : \n{cleaned_2}")
