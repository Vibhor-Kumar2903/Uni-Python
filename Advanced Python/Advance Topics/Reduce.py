#WAP to filter a sequence
from functools import reduce

li = [1,2,3,4,5]
def add(x,y):
    return x+y

res = reduce(add, li)
print(f"\nAfter filter : {res}")

#WAP to filter a sequence
li = [1,2,3,4,5,6,7,8,9]
res = reduce(lambda x,y: x+y, li)
print(f"\nAfter filter : {res}")



