"""
Самое длинное слово.

Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
"""

my_str = "Днём позже, днём раньше - какая разница."
punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]

for i in punctuation:
    my_str = my_str.replace(i, '')

words = my_str.split(' ')

long = 0
word = words[0]

for i in words:
    if len(i) > long:
        long = len(i)
        word = i

print('Самое длинное слово : ', word)
