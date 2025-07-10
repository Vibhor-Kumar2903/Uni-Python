import numpy as np

arr_1d = np.array([[1,2,3,4]])
arr_2d = np.array([[1,2,3,4],[7,8,9,4]])
arr_3d = np.array([[[1,2,3,4],[7,8,9,4],[10,20,30,40]]])

print(f"Dimension of given array : {arr_1d.ndim}")
print(f"Dimension of given array : {arr_2d.ndim}")
print(f"Dimension of given array : {arr_3d.ndim}")