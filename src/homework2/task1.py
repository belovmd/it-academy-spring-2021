M = int(input('Введите стоимость (рублей) : '))
N = int(input('Введите стоимость (копеек) : '))
S = int(input('Введите количество товара (шт.) : '))
L = int(input('Введите количество покупаемого товара (шт.) : '))

price_one_item = (M * 100 + N) / S
M_L = int(price_one_item * L) // 100
N_L = int(price_one_item * L) % 100

print('Общая цена ', M_L, 'рублей', N_L, 'копеек')
