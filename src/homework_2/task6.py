number = int(input("Введите целое число: "))
number2 = number
finish_number = 0

while number2 > 0:
    itr = number2 % 10
    number2 = number2 // 10
    finish_number = finish_number * 10
    finish_number = finish_number + itr

if number == finish_number:
    print('палиндром')

else:
    print('не палиндром')
