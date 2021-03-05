"""Homework2 - task1

Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек цена, а также количество S товара.
Посчитайте общую цену в рублях и копейках за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек

"""


M = 3
N = 20
S = 3

price = M + N / 100
total_cost = S * price

print('Total cost = {p1} items * {p2} rubles = {p3} rubles {p4} pennies'.format(
    p1=S,
    p2=price,
    p3=int(total_cost // 1),
    p4=int(total_cost % 1 * 100)))
