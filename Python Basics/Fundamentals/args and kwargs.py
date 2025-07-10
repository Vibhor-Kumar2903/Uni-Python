def args_function(*args):
    return sum(args)

print(args_function(1,2,2,3,6))

def kwargs(**kwargs_arg):
    for key, value in kwargs_arg.items():
        print(f"{key} :: {value}")

print(kwargs(a=1, b=2, c=3))