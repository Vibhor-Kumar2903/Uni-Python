#WAP to print square of each element
li_1 = [1,2,3,4,5,6]
new_li = [num**2 for num in li_1]
print(f"\nSquare of each element :")
print(new_li)

#WAP to print triple of each element
li_2 = [1,2,3,4,5,6]
new_li = [num*2 for num in li_2]
print(f"\nTriple of each element :")
print(new_li)

#WAP to print double of odd number only
li_3 = [1,2,3,4,5,6]
new_li = [num*2 for num in li_3 if num%2!=0]
print(f"\nDouble of odd element :")
print(new_li)

#WAP to print natural numbers upto.
series = [i for i in range(1,10)]
print(f"\nNatural numbers :")
print(series)

#WAP to print coordinates upto 3.
cod = [(x,y) for x in range(4) for y in range(4)]
print(f"\nCoordinates :")
print(cod)

#WAP to print flattening a matrix.
matrix = [[1,2,3], [4,5], [6,7,8], [9]]
flat = [col for row in matrix for col in row]
print(f"\nFlattening the given matrix :")
print(flat)

#WAP to print capitalization of list element and flattening a matrix.
matrix = [['apple', 'banana', 'cherry'],
          ['date', 'fig', 'grape'],
          ['kiwi', 'lemon', 'mango']]

modified_element = [[fruit.capitalize() for fruit in row] for row in matrix ]
print(f"\nCapitalizing the given matrix elements:")
print(modified_element)

modified_element = [fruit.capitalize() for row in matrix for fruit in row]
print(f"\nCapitalizing & flattening the given matrix elements:")
print(modified_element)


#WAP to print flattening a matrix and print upto a range.
matrix = [[1,2,3], [4,5], [6,7,8], [9]]
flat = [num for row in matrix for num in row]
print(f"\nFlattening the given matrix:")
double = [num**2 for num in flat[:3]]
print(double)



