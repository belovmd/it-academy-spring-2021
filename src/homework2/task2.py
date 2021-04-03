"""Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания."""


def find_max_word(str_):
    formatted_string = "".join(letter for letter in str_ if letter.isalpha() or letter.isspace() or letter.isdigit())
    lst = formatted_string.split()
    big_word = lst[0]
    for word in lst:
        if len(big_word) < len(word):
            big_word = word
    return print("Самое длинное слово в предложении:", big_word)


find_max_word('dadldksdj2323(*@^*@& dsad)()"|}"|??}@ dsldk123')
