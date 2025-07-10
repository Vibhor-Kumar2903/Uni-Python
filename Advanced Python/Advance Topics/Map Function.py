#Convert a sequence of string to int.
s = ['1','2','3','4','5']
res = map(int, s)
print(f"\nAfter Mapping : {list(res)}")


#Double the element of a sequence.
a = [1, 2, 3, 4, 5]
def double(n):
    return n*2

res = map(double, a)
print(f"\nAfter Mapping : {list(res)}")


#Sqaure the element of a sequence.
a = [1, 2, 3, 4, 5]
res = map(lambda x: x**2, a)
print(f"\nAfter Mapping : {list(res)}")


#Handle multiple sequences.
a = [1,2,3,4,5]
b = [11,22,33,44,55]

res = map(lambda x,y : x+y, a,b)
print(f"\nAfter Mapping : {list(res)}")


#Capitalized the sequence element
seq = ['apple', 'banana', 'cherry']
res = map(lambda a: a.upper(), seq)
print(f"\nAfter Mapping : {list(res)}")


