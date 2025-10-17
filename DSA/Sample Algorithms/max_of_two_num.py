def max_func_version1(a, b):
    return max(a,b)

def max_func_version2(a,b):
    return a if a>b else b

def max_func_version3(a,b):
    if a>b:
        return a
    else:
        return b

def max_func_version4(a,b):
    result = lambda a,b : a if a>b else b
    return result(a,b)

def max_func_version5(a,b):
    L = []
    L.append(a)
    L.append(b)
    return max(L)


print(f"Max function version 1 : {max_func_version1(5,6)}")
print(f"Max function version 2 : {max_func_version2(5,6)}")
print(f"Max function version 3 : {max_func_version3(5,6)}")
print(f"Max function version 4 : {max_func_version4(5,6)}")
print(f"Max function version 5 : {max_func_version5(5,6)}")



