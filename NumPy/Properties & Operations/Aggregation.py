import numpy as np

arr = np.array([10,20,30,40,50,60,60,50,10])

print(f"Sum of array elements : {arr.sum()}")

print(f"Mean of array elements : {(arr.mean()).round(2)}")

print(f"Max in array elements : {arr.max()}")

print(f"Min in array elements : {arr.min()}")

print(f"Standard Deviation in array elements : {(arr.std()).round(2)}")

print(f"Variance in array elements : {(arr.var()).round(2)}")
