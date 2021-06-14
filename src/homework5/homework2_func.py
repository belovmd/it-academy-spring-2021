def triangle():
    a, b, c = int(input()), int(input()), int(input())
    if a + b > c and b + c > a and a + c > b:
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print('Треугольник существует, его площадь равна {} у.е.'.format(s))
    else:
        print('Неверные данные')


def palindrome():
    seed = int(input('Введите число произвольное число: '))
    check_number = seed
    num_finish = 0
    while seed > 0:
        num_finish = (10 * num_finish) + seed % 10
        seed //= 10
    if check_number == num_finish:
        print('Палиндром')
    else:
        print('Число не является Палиндромом')


def fibonacci_number():
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
