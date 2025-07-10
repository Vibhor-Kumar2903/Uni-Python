prices = [100,200,300,400,500]
discount = 10

discounted_price = []
for price in prices:
    d_price = (price - price * discount/100)
    discounted_price.append(d_price)

print(discounted_price)
