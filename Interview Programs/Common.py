import operator
import  math

from Tools.scripts.pathfix import preserve_timestamps


class BasicPrograms:
    @staticmethod
    def add_two_numbers():
        num1 = int(input("First number = "))
        num2 = int(input("Second number = "))

        op_res = num1+num2
        result_1 = f"Sum of {num1} & {num2} is {op_res}"
        print(result_1)

        lam_res = lambda a,b : a+b
        result_2 = (lam_res(num1, num2))
        result_2 = f"Sum of {num1} & {num2} is {result_2}"
        print(result_2)

        func_res = operator.add(num1,num2)
        result_3 = f"Sum of {num1} & {num2} is {func_res}"
        print(result_3)

        #return result_1, result_2, result_3
        #return op_res, result_2, func_res

    @staticmethod
    def max_two_num():
        num1 = input("First numbers = ")
        num2 = input("Second number = ")

        result = max(num1, num2)
        print(f"Greater number between {num1} & {num2} is {result}")

    @staticmethod
    def factorial():
        num = int(input("Enter the number = "))

        fact = 1
        for i in range(1, num+1):
            fact = fact * i

        print(f"Factorial of {num} is {fact}")


    @staticmethod
    def simple_interest():
        amt = int(input("Enter principle amount = "))
        rate = int(input("Enter rate of interest = "))
        time = int(input("Enter time duration = "))

        SI = (amt*rate*time)/100
        #SI = lambda p, r, t: p*r*t
        t_amt = SI+amt
        print(f"Simple Interest : {SI}")
        print(f"Total amount  : {t_amt}")


    @staticmethod
    def compound_interest():
        p_amt = float(input("Enter principle amount = "))
        rate = float(input("Enter rate of interest = "))
        time = float(input("Enter time duration = "))

        amt = p_amt * (pow((1 + rate/100), time))
        amt = round(amt, 2)
        print(f"Total amount : {amt}")

        CI = amt-p_amt
        CI = round(CI, 2)
        print(f"Compound interest : {CI}")

    @staticmethod
    def armstrong_number():
        num = int(input("Enter the test number : "))
        temp = num
        summ = 0

        while temp!=0:
            remainder = temp%10
            summ = summ + pow(remainder, 3)
            temp = temp//10

        if num == summ:
            print("Given number is an armstrong number.")
        else:
            print("Given number is NOT an armstrong number.")


    @staticmethod
    def area_of_circle():
        radius = int(input("Enter the radius of circle in cm = "))
        area = math.pi * (pow(radius,2))
        area = round(area, 2)
        print(f"Area of circle = {area} cm2")

    @staticmethod
    def prime_numbers_in_range():
        print("Enter the range")
        s_point = int(input("Enter the starting number : "))
        e_point = int(input("Enter the ending number : "))

        print(f"\nBelow are the Prime numbers between {s_point} & {e_point} : ")

        for num in range(s_point, e_point+1):
            if num <= 0:
                continue
            if num > 1:
                for i in range(2, num):
                    if num%i == 0:
                        break
                else:
                    print(f"{num} ", end='  ')


    @staticmethod
    def prime_number():
        num = int(input("Enter the test number : "))

        if num <= 0:
             print(f"{num} is an invalid number.")

        else:
            for i in range(2, num):
                if num%i==0:
                    break
                else:
                    print(f"{num} is NOT a Prime Number.")
                    break
            else:
                print(f"{num} is a Prime Number.")


    @staticmethod
    def fibonacci_series():
        num = int(input("Enter the Nth number : "))
        start = 0
        fib = 1
        count = 0

        if num <= 0:
            print(f"{num} is not a valid number. Please enter a positive number.")

        elif num == 1:
            print(f"Fibonacci series upto {num} term is : \n{start}")

        else:
            print(f"Fibonacci series upto {num} term is :")
            while count<num:
                print(f"{start}", end=' ')
                summ = start + fib
                start = fib
                fib = summ
                count+=1


    @staticmethod
    def ASCII_value():
        char = input("Enter the character : ")
        print(f"ASCII value of '{char}' is : {ord(char)}")

        sym = int(input("Enter a symbol or digit : "))
        print(f"Character for given symbol or digit is : {chr(sym)}")


    @staticmethod
    def sum_of_square():
        nTerm = int(input("Enter the nth term : "))
        count = 0
        summ = 0

        if nTerm <= 0:
            print("Please enter any natural number.")

        elif nTerm >= 1:
            """
            while count!=nTerm:
                count+=1
                summ = summ + pow(count, 2)

            print(f"Sum of square of first n natural number till {nTerm} is = {summ}")
            """

            for i in range (1, nTerm+1):
                summ = summ + pow(i,2)

            print(f"Sum of square of first n natural number till {nTerm} is = {summ}")


    @staticmethod
    def sum_of_cube():
        term = int(input("Enter the nth term : "))
        summ = 0

        if term<=0:
            print("Please enter a natural number.")

        elif term >= 1:
            for i in range(1, term+1):
                summ = summ + pow(i,3)

            print(f"Sum of cube of first n natural number is : {summ}")


    @staticmethod
    def without_new_line():
        #method_1
        print("Vibhor", end=' ')
        print("Kumar")

        name_list = ['vibhor', 'kumar']
        print(" ".join(name_list))

        name_list = ['vibhor', 'kumar', 'Maurya']
        print(*name_list)















#BasicPrograms.add_two_numbers()
#BasicPrograms.max_two_num()
#BasicPrograms.factorial()
#BasicPrograms.simple_interest()
#BasicPrograms.compound_interest()
#BasicPrograms.armstrong_number()
#BasicPrograms.area_of_circle()
#BasicPrograms.prime_numbers_in_range()
#BasicPrograms.prime_number()
#BasicPrograms.fibonacci_series()
#BasicPrograms.ASCII_value()
#BasicPrograms.sum_of_square()
#BasicPrograms.sum_of_cube()
BasicPrograms.without_new_line()