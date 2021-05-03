"""Homework2 - task1

Напишите программу, которая считает общую цену. Вводится M рублей
и N копеек цена, а также количество S товара Посчитайте общую цену
в рублях и копейках за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек
"""

import re

input_string = "Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета."
numbers_lst = (re.findall(r"\d+", input_string))

goods_amount = int(numbers_lst[2])
rubles = int(numbers_lst[0]) * goods_amount
penny = int(numbers_lst[1]) * goods_amount

print("Общая цена {r} рублей {p} копеек".format(r=rubles, p=penny))
