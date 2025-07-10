import numpy as np

"""
vstack() = vertical stack = row wise
hstack() = horizontal stack = column wise
"""

arr_1 = np.array([1,2,3,4])
arr_2 = np.array([5,6,7,8]) 

print(f"\nVertical Stack : \n{np.vstack((arr_1, arr_2))}")
print(f"\nHorizontal Stack : \n{np.hstack((arr_1, arr_2))}")
 