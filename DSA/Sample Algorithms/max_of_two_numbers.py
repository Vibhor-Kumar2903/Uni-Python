#WAP to return the max of two numbers
def with_max_function_V1(a,b):
    return max(a,b)

def with_if_else_V2(a,b):
    return a if a>b else b

def with_if_else_ladder_V3(a,b):
    if a>b:
        return a
    else:
        return b

def with_lambda_function_V4(a,b):
    result = lambda a,b: a if a>b else b
    return result(a,b)

a = input()
b = input()

print(f"V1 :",with_max_function_V1(a,b))
print(f"V2 : {with_if_else_V2(a,b)}")
print(f"V3 : {with_if_else_ladder_V3(a,b)}")
print(f"V4 : {with_lambda_function_V4(a,b)}")

