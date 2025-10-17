def min_func_version1(a, b):
    return min(a,b)

def min_func_version2(a,b):
    return a if a<b else b

def min_func_version3(a,b):
    if a<b:
        return a
    else:
        return b

def min_func_version4(a,b):
    result = lambda a,b : a if a<b else b
    return result(a,b)

def min_func_version5(a,b):
    L = []
    L.append(a)
    L.append(b)
    return min(L)


print(f"Min function version 1 : {min_func_version1(5,10)}")
print(f"Min function version 2 : {min_func_version2(5,10)}")
print(f"Min function version 3 : {min_func_version3(5,10)}")
print(f"Min function version 4 : {min_func_version4(5,10)}")
print(f"Min function version 5 : {min_func_version5(5,10)}")



