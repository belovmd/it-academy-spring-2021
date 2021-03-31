# Task 1. Напишите программу, которая считает общую цену. Вводится M рублей и
# N копеек цена, а также количество S товара. Посчитайте общую цену в рублях и
# копейках за L товаров.
# Пример: Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
# Output: Общая цена 9 рублей 60 копеек.

price = [int(num) for num in input("Введите рубли, копейки и "
                                   "количество товара через пробел: ").split()]

# the list of 3 int corresponded to rubles, pennies & goods is hidden
# under "price"

rubles, pennies, goods = price[0], price[1], price[-1]
sum_rubles = rubles * goods + ((pennies * goods) // 100)
sum_pennies = pennies * goods % 100

print("Общая цена товаров:{} рублей {} копеек".format(sum_rubles, sum_pennies))
