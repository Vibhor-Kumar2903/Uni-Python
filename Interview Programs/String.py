from itertools import count


class StringExercise:
    #Check whether the string is Symmetrical or Palindrome
    @staticmethod
    def palindrome():
        str = input("Enter a string : ")
        d_str = str[::-1]

        if d_str == str:
            print("Given string is a palindrome.")
        else:
            print("Given string is NOT a palindrome.")

    @staticmethod
    def length_of_string():
        str = input("Enter a string : ")

        print(f"Length of string = {len(str)}")

        count = 0
        for i in str:
            count+=1

        print(f"Length of string = {count}")

    @staticmethod
    def reverse_the_word():
         pass




#StringExercise.palindrome()
StringExercise.length_of_string()