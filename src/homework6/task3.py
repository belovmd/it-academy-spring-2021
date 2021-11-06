# Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи
# алгоритма Евклида (мы не знаем функции и рекурсию).
# HomeWork4 task7
# Оформите указанную задачу из прошлых домашних в виде функции и покройте тестами.
# Учтите, что в функцию могут быть переданы некорректные значения, здесь может пригодится
# ‘assertRaises’. Не нужно переделывать функцию для того чтобы она ловила все возможные ситуации сама.


def numbers(first_num, second_num):
    # Мои исправления на основании тестов
    # if type(first_num) is not int or type(second_num) is not int:
    #     raise TypeError('Некорректный тип данных')
    # if first_num < 1 or second_num < 1:
    #     raise ValueError('Число не натуральное')
    if first_num < second_num:
        first_num, second_num = second_num, first_num
    elif first_num == second_num:
        return first_num

    while first_num > second_num:
        first_num = first_num % second_num
        if first_num:
            first_num, second_num = second_num, first_num
        else:
            return first_num + second_num
