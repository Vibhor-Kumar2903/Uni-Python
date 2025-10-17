def find_palindromic_substrings(str):
    result = []
    no_of_alphabets = len(str)

    for i in range(no_of_alphabets):
        for j in range(i + 2, no_of_alphabets+1):  # substrings of length >= 2
            sub = str[i:j]
            if sub == sub[::-1]:
                result.append(sub)
    return result


# Example usage
input_str = "mamadsfajsdfmalayalamasdfsafmadam"
output = find_palindromic_substrings(input_str)
print(output)