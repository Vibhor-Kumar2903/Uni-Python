import numpy as np

arr_1D_1 = np.array([1,2,3,4])
print(arr_1D_1)
arr_1D_2 = np.array([5,6,7,8])
print(arr_1D_2)

new_arr = np.concatenate((arr_1D_1, arr_1D_2), axis=0)
print(new_arr)

arr_2D_1 = np.array([[1,2], [3,4]])
print(arr_2D_1)
arr_2D_2 = np.array([[5,6], [7,8]])
print(arr_2D_2)


new_arr = np.concatenate((arr_2D_1, arr_2D_2), axis=0)
print(new_arr)
