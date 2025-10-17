class StringIndex:
    input_string = input("Enter a string : \n")

    def even_index_conversion(self):
        string_list = list(self.input_string.lower())

        for i in range(len(string_list)):
            if i % 2 == 0:
                string_list[i] = string_list[i].upper()
        return ''.join(string_list)

    def odd_index_conversion(self):
        string_list = list(self.input_string.lower())

        for i in range(len(string_list)):
            if i % 2 != 0:
                string_list[i] = string_list[i].upper()
        return ''.join(string_list)


si = StringIndex()
odd_result = si.odd_index_conversion()
print(f"\nOdd_result : {odd_result}")
even_result = si.even_index_conversion()
print(f"\nEven_result : {even_result}")
