"""
Homework2 (task1)
"""
COUNT = int(input('Введите колличество товара: '))
RUB, KOP = 3, 40
total_price = (RUB * 100 + KOP) * COUNT
print(f'Общая цена товара {total_price // 100} рублей {total_price % 100} копеек')
