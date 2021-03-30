# Task 5. Выведите n-ое число Фибоначчи, используя только временные переменные,
# циклические операторы и условные операторы. n - вводится

number = int(input("Введите n-ое число Фибоначчи: "))
f_num1, f_num2, counter = 0, 1, 0

while counter != number - 2:
    f_variable = f_num1 + f_num2
    f_num1 = f_num2
    f_num2 = f_variable
    counter += 1

print(number, "число в последовательности Фибоначчи —", f_num2)
