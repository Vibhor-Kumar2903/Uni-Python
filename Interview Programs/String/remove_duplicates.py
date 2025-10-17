def remove_duplicates_alphabets(str):
    print(f"\nOriginal string : {str}")
    str = str.lower()
    unique_alpha = set(str)
    print(f"\nUnique alpha, unordered : {unique_alpha}")
    ordered_alpha = "".join(dict.fromkeys(str))
    print(f"\nUnique alpha, ordered : {ordered_alpha}")



given_string = "MyNameIsKhan"
remove_duplicates_alphabets(given_string)


def remove_duplicates_words(str):
    print(f"\nOriginal string : {str}")
    str = str.lower()
    word = str.split(' ')

    unique_word = []

    for i in range(word):
        for j in range(word):
            if not word[i]==word[j]:
                unique_word.append(word[i])

    print()






# given_string = "MyNameIsKhan"
given_string = "My Name Is Khan and His Name Is King"
remove_duplicates_alphabets(given_string)