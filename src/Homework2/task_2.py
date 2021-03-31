# Task 2. Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.

import string

orig_str = "Добро и зло — понятия относительные, и люди просто " \
           "приспосабливают их к своим целям."

words = (orig_str.translate(str.maketrans('', '', string.punctuation))).split()
longest = ""

for element in words:
    if len(element) > len(longest):
        longest = element

print(longest)
