# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.
import string
str_ = "A string of words is entered, separated by spaces and punctuation!!! marks"
for mark in string.punctuation:
    str_ = str_.replace(mark, "")

worlds = str_.split()
longest_word = ""
for word in worlds:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)
