# 5. Выведите n-ое число Фибоначчи, используя только временные переменные,
# циклические операторы и условные операторы.
# n - вводится

# ------------------------------------------------------------------------------------ #

# using "for"
# For example: I would like to print 10 fibonacci numbers
a = 1  # pre-previous number
b = 1  # previous number
for i in range(10):
    n = a + b
    a = b
    b = n
    print(i, n)
