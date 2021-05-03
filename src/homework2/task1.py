"""
Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек цена, а также количество S товара.
Посчитайте общую цену в рублях и копейках за L товаров.
"""

M = int(input('Введите количество рублей (M): '))
N = int(input('Введите количество копеек (N): '))
S = int(input('Введите количество товара (S): '))

print('Общая цена за', S, 'шт. составляет', M, 'рублей(-я)', N, 'копеек')

price_for_one_item_cents = ((M * 100) + N) / S

L = int(input('Для расчета стоимости введите количество покупаемых товаров (L): '))

rubles_for_another_quantity = int((price_for_one_item_cents * L) // 100)
price_for_one_item_cents = int((price_for_one_item_cents * L) % 100)

print('Общая цена за', L, 'шт. составляет', rubles_for_another_quantity, 'рублей(-я)',
      price_for_one_item_cents, 'копеек')
