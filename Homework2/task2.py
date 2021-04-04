# 2. Найти самое длинное слово в введенном предложении. Учтите что в
# предложении есть знаки препинания.

znaki_prep = ".?!,-;:"

max_len = 0
max_word = []

txt = input("Найти самое длинное слово в предложении. Введите предложение:")

for letter in txt:
    if letter in znaki_prep:
        txt = txt.replace(letter, " ")

for word in txt.split():
    count_letter = len(word)
    if count_letter > max_len:
        max_len = count_letter
        max_word = [word]
    elif count_letter == max_len:
        max_word.append(word)
print('самое длинное слово', max_word, 'состоит из', max_len, 'букв')
