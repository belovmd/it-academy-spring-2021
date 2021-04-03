"""Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.

Учитывать только английские буквы.
"""

my_string = input("Введите предложение: ")
low_count = 0
up_count = 0
up_letters = "ASDFGHJKLQWERTYUIOPZXCVBNM"
low_letters = "asdfghjklzxcvbnmqwertyuiop"
for letter in my_string:
    if letter in up_letters:
        up_count += 1
    elif letter in low_letters:
        low_count += 1
    else:
        pass
print("Больших букв в строке:" + str(up_count) + " маленьких букв: " + str(low_count))
