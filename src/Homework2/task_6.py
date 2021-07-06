"""
Homework2 (task_6)

Определить числа палиндромы


"""

number = int(input("Введите целое положительное число: "))
temp = number
reverse_number = 0
while number > 0:
    last_digit = number % 10
    number = number // 10
    reverse_number = reverse_number * 10 + last_digit
if reverse_number == temp:
    print("Число палиндром")
else:
    print("Не палиндром")
