number = int(input('Введите номер числа Фибоначчи: '))
first_number = 0
second_number = 1
step = 2
if number == 1:
    print('Ваше число:', 0)
elif number == 2:
    print('Ваше число: ', 1)
else:
    while step != number:
        new_number = first_number + second_number
        first_number, second_number = second_number, new_number
        step += 1
    # noinspection PyUnboundLocalVariable
    print('Ваше число:', new_number)
