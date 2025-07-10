#WAP to print cube of given number
cube = lambda num : num**3
print(f"\nCube : {cube(10)}")

#WAP to print addition of given numbers
addition = lambda a,b,c : a+b+c
print(f"\nAddition : {addition(10,20,30)}")

#WAP to print multiplication of given numbers
multiply = lambda a,b : a*b
print(f"\nMultiplication : {multiply(10,20)}")

#WAP to use lambda function inside a python function
def my_func(n):
    return lambda num : num*n

doubler = my_func(2)
tripler = my_func(3)

print(f"\nDoubler : {doubler(10)}")
print(f"\nTripler : {tripler(10)}")


