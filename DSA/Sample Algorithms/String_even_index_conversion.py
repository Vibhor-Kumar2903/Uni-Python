# WAP to read a string and convert all the even index values into upper case.

def even_index_case_conversion(s):
    l = list(s.lower())
    convert_l = []
    for i in range(len(l)):
        if i%2 == 0:
            l[i] = l[i].upper()
        convert_l.append(l[i])
    return ''.join(convert_l)


fetch_string = input("Enter your string :  ")
converted_string = even_index_case_conversion(fetch_string)
print(f"Converted string : {converted_string}")

