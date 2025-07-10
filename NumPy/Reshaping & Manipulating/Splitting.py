import numpy as np

"""
np.split() = For splitting the array in equal split
np.hsplit()
np.vsplit()
"""

arr = np.array([10,20,30,40,50,60,70,80])

equal_split = np.split(arr,2)
print(f"\nEqual split : \n{equal_split}")