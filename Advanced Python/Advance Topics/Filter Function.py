#WAP to filter a sequence
li = [1,2,3,4,5,6,7,8,9,10]
def odd(n):
    return n%2!=0

res = filter(odd, li)
print(f"\nAfter filter..")
print(list(res))

#WAP to filter a sequence
li = [1,2,3,4,5,6,7,8,9,10,11,12]
res = filter(lambda x: x*2, li)
print(f"\nAfter filter..")
print(list(res))

#WAP to filter a sequence
li = [1,2,3,4,5,6,7,8,9,10,11,12]
res = filter(lambda x: x%2==0, li)
print(f"\nAfter filter..")
print(list(res))


