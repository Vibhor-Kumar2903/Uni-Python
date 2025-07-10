#WAP to print square dictionary
square_dict = {num : num**2 for num in range(1,5)}
print(f"\nSquare_dict : {square_dict}")

#WAP to print a dictionary using two list.
key = ['A', 'B', 'C', 'D', 'E', 'F']
value = [1,2,3,4,5,6]

dict_1 = {k:v for (k,v) in zip(key, value)}
print(f"\nZIP Dict : {dict_1}")

cube_dict = {num : num**3 for num in range(1,11)}
print(f"\nCube Dict : {cube_dict}")

conditional_dict = {num : num*2 for num in range(10) if (num*2)%2==0}
print(f"\nconditional Dict : {conditional_dict}")

L = "GFG"
dict = {x: {y:x+y for y in L} for x in L}
print(f"\nDict : {dict}")







