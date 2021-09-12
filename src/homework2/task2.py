# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.

str_ = 'Привет, безумный мир.'

marks = '''!()-[]{};?@#$%:'"\,./^&amp;*_'''

for letter in str_:
    if letter in marks:
        new_str = str_.replace(letter, '')

words = new_str.split()
long_word = ""

for word in words:
    if len(word) > len(long_word):
        long_word = word
print(long_word)
