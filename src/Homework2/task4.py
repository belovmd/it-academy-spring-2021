string = input()
lowercase_letter = 0
big_letter = 0
for letter in string:
    if letter.islower():
        lowercase_letter += 1
    elif letter.isupper():
        big_letter += 1
print(('Количество строчных букв: ', lowercase_letter,
       '\n' 'Количество прописных букв: ', big_letter))
