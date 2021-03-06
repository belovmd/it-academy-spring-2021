my_string = input("Введите предложение: ").split()
formatted_string = []
for word in my_string:
    if word[len(word) - 1] == ',' or word[len(word) - 1] == '.' or word[len(word) - 1] == ':' \
            or word[len(word) - 1] == '!' \
    or word[len(word) - 1] == '?' or word[len(word) - 1] == '-':
        formatted_string.append(word[:-1])
    else:
        formatted_string.append(word)
big_word = formatted_string[0]
for word in formatted_string:
    if len(big_word) < len(word):
        big_word = word
print("Самое длинное слово в предложении:", big_word)
