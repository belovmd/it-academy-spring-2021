"""
Homework 5 - Task6
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


x = int(input("Введите число: "))
y = x
val = 0

while x > 0:
    x = x >> 1
    if not y % (2 ** val):
        max_result = 2 ** val
    val += 1

print("{}({})".format(y, max_result))
