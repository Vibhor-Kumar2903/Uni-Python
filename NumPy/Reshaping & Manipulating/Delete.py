import numpy as np

"""
axis=1 =>> Column
axis=2 =>> Row
"""

arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr)

del_arr = np.delete(arr, 1, axis=None)
print(del_arr)

arr_2D = np.array([[1,2], [3,4]])
print(arr_2D)

del_arr = np.delete(arr_2D, 0, axis=1)
print(del_arr)