# WAP to read a string and convert all the ODD index values into upper case.

def odd_index_value_conversion(s):
    l = list(s.lower())
    for i in range(len(l)):
        if i%2 != 0:
            l[i] = l[i].upper()
    return ''.join(l)


fetch_string = input(f"Enter a string :  ")
result = odd_index_value_conversion(fetch_string)
print(f"Converted string : {result}")


