# 1. Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
# кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
# одновременно кратных и 3 и 5 - FizzBuzz
lst = []
count_number = 1

while count_number != 101:
    if count_number % 3 == 0 and count_number % 5 == 0:
        lst.append('FizzBuzz')
    elif count_number % 3 == 0:
        lst.append('Buzz')
    else:
        lst.append(count_number)

    count_number += 1

print(lst)
