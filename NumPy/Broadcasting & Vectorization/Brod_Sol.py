import numpy as np

price_arr = np.array([100,200,300,400,500])
discount = 10

d_price = price_arr - (price_arr*discount/100)
print(f"\nDiscounted price : \n{d_price}")
