"""
Самое длинное слово.

Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
"""
import string

my_str = "Днём позже, днём раньше - какая разница."
my_str = "".join(ch_ for ch_ in my_str if ch_ not in string.punctuation)

words = my_str.split(' ')

long = 0
longest_word = words[0]

for word in words:
    if len(word) > long:
        long = len(word)
        longest_word = word

print('Самое длинное слово :', word)
