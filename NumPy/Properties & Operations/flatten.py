import numpy as np

"""
np.ravel() - It will create a view
np.flatten() - It will create a copy
"""

arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr)

print(arr.ravel())

print(arr.flatten())



