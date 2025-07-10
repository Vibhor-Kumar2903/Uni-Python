""" difference between local and global variable """


def function_1():
    string_s = "Dell"
    print(f"Inside function : {string_s}")


#function_1()
#print(f"string_s : {string_s}") #NameError: name 'string_s' is not defined

g_str = "Macbook"
def function_2():
    string_s = "Dell"
    print(f"Inside function  : {string_s}")
    print(f"Inside function : {g_str}")

# function_2()
# print(f"Outside global : {g_str}")
# print(f"Outside local : {string_s}") #NameError: name 'string_s' is not defined


g2_str = "Macbook"
def function_3():
    #string_s += "Dell" #UnboundLocalError: cannot access local variable 'string_s' where it is not associated with a value
    print(f"Inside function  : {string_s}")
    print(f"Inside function : {g_str}")

function_3()
# print(f"Outside global : {g_str}")


