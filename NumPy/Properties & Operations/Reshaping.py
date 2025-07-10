import numpy as np

arr = np.array([10,30,40,50,60,60,50,10, 70, 80, 90, 10])
print(arr)

reshaped_arr_1 = arr.reshape(2,6)
print(f"\n{reshaped_arr_1}")

reshaped_arr_2 = arr.reshape(3,4)
print(f"\n{reshaped_arr_2}")


