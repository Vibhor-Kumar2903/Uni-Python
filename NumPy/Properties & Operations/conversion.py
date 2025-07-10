import numpy as np

arr = np.array([7,8,9.5,4])
print(arr)
print(f"Data type of given array : {arr.dtype}")

new_arr = arr.astype(int)

print(f"Convert the data type of arr : \n{new_arr}")
print(f"Data type of given array : {new_arr.dtype}")

