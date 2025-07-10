import numpy as np

arr = np.array([1,2,3,np.inf,4,-np.inf,6])
print(f"\nArr : \n{arr}")

print(np.isinf(arr))

cleared_arr = np.nan_to_num(arr, posinf=100, neginf=200)
print(f"\nCleared_arr : \n{cleared_arr}")

