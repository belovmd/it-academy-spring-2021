# Оформите решение задач из прошлых домашних работ в функции.

# Напишите программу, которая считает общую цену. Вводится M рублей и N копеек цена,
# а также количество S товара Посчитайте общую цену в рублях и копейках за L товаров.
def task1():
    rubles = int(input('ВВедите количество рублей: '))
    penny = int(input('ВВедите количество центов: '))
    num_goods = int(input('ВВедите количество товара: '))
    kop = (penny * num_goods) % 100
    whole_kop = int((penny * num_goods) / 100)
    rub = (rubles * num_goods) + whole_kop

    print('Общая цена: ', rub, 'рублей', kop, 'копеек')


# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.
def task2():
    str_ = str(input('введите строку'))
    marks = '''!()-[]{};?@#$%:'",./^&amp;*_'''
    new_str = ''

    for letter in str_:
        if letter in marks:
            new_str = str_.replace(letter, '')

    words = new_str.split()
    long_word = ""

    for word in words:
        if len(word) > len(long_word):
            long_word = word
    print(long_word)


# Вводится строка. Требуется удалить из нее повторяющиеся
# символы и все пробелы. Например, если было введено "abc cde def",
# то должно быть выведено "abcdef"
def task3():
    str_ = str(input('введите строку'))
    str_new = ''
    for i in str_:
        if i not in str_new and i != ' ':
            str_new += i

    print(str_new)


# Посчитать количество строчных (маленьких) и прописных (больших)
# букв в введенной строке. Учитывать только английские буквы.
def task4():
    str_ = str(input('введите строку: '))
    big_letter = 0
    small_letter = 0
    for i in str_:
        if 'A' <= i <= 'Z':
            big_letter += 1
        if 'a' <= i <= 'z':
            small_letter += 1

    print('Прописные', big_letter)
    print('Строчные', small_letter)


# Выведите n-ое число Фибоначчи, используя только временные переменные,
# циклические операторы и условные операторы. n - вводится
def task5():
    num = int(input('введите число: '))
    if 0 < num < 3:
        print(1)
    else:
        fib1 = 1
        fib2 = 1
        fib3 = 0
        i = 2
        while i < num:
            (fib3, fib2, fib1) = (fib2 + fib1, fib3, fib2)
            i += 1
            continue
        print(fib3)


# Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
# Число положительное целое, произвольной длины.
# Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще)
def task6():
    num = int(input('введите число: '))
    start_num = num
    revers_num = 0

    while num > 0:
        remainder = num % 10
        num = num // 10
        revers_num = revers_num * 10
        revers_num = revers_num + remainder

    if (start_num - revers_num) == 0:
        print('палиндром')
    else:
        print('No!')


#  Даны: три стороны треугольника. Требуется: проверить, действительно ли это стороны треугольника.
#  Если стороны определяют треугольник, найти его площадь.
#  Если нет, вывести сообщение о неверных данных
def task7():
    a = int(input('введите сторону треугольника: '))
    b = int(input('введите сторону треугольника: '))
    c = int(input('введите сторону треугольника: '))
    p = (a + b + c)
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

    if (a + b) > c and (b + c) > a and (c + a) > b:
        print('Площадь треугольника: ', s)
    else:
        print('неверные данные')
