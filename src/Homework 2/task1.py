"""
Homework 2 (task 1)

Напишите программу, которая считает общую цену. Вводится M рублей и N копеек цена
, а также количество S товара Посчитайте общую цену в рублях и копейках за L товаров.


"""


def counter_float(count, price):  # уменьшить колличество вводимых переменных упостить расчет
    return int(count) * float(price)


input_price = float(input('Введите цену товара (руб.коп): '))
input_count = int(input('Введите колличество товара: '))
print("Общая сумма за", input_count, "товаров", counter_float(input_count, input_price))
