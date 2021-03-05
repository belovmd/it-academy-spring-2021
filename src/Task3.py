def remove_repetition(sentence):
    resulting_str = ''
    str_to_check = sentence.replace(' ', '')
    while len(str_to_check):
        resulting_str += str_to_check[0]
        str_to_check = str_to_check.replace(str_to_check[0], '')
    return resulting_str


# TEST
print(remove_repetition("abc cde def"))
