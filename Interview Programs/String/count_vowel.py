def count_vowels(str):
    v_list = ['a','e','i','o','u']
    l_str = list(str)

    count = 0

    for i in range(len(l_str)):
        if l_str[i] in v_list:
            count+=1

    print(f"\nNumber of vowels : {count}")



sample_string = "my name is khan"
count_vowels(sample_string)
