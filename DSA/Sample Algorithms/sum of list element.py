#WAP to all the elements of the list

import functools

def with_for_loop(l):
    s = 0
    for i in range(len(l)):
        s = s+l[i]
    return s

def with_sum_function(l):
    return sum(l)

def with_functools_function(l):
    summ = functools.reduce(lambda i,j : i+j, l)
    return summ


num_list = [10,20,30,40,50]

print(f"Sum of list : {with_for_loop(num_list)}")
print(f"Sum of list : {with_sum_function(num_list)}")
print(f"Sum of list : {with_functools_function(num_list)}")
