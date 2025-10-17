def remove_vowels(given_str):
    v_list = ['a','e','i','o','u']
    s_list = list(given_str)
    required = []

    for i in range(len(s_list)):
        if s_list[i] not in v_list:
            required.append(s_list[i])

    output = ''.join(required)
    output = output.title()
    print(output)

given_string = 'My name is Khan'

remove_vowels(given_string)
