
'''
1. Напишите программу, которая считает общую цену. Вводится M рублей и N копеек цена,
а также количество S товара Посчитайте общую цену в рублях и копейках за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек
Задачу поместите в файл task1.py в папке src/homework2.
'''


def calculate_total_price(*price):
    total_price = dict()
    total_price["рубли"] = 0
    total_price["копейки"] = 0
    for current_element in price:
        local_dict = parse_price(current_element)
        total_price["рубли"] += local_dict["рубли"]
        total_price["копейки"] += local_dict["копейки"]
        while total_price["копейки"] >= 100:
            count_ruble = total_price["копейки"] // 100
            total_price["рубли"] += count_ruble
            total_price["копейки"] = total_price["копейки"] % 100
    string_result = "Общая цена {} рублей {} копеек".format(total_price["рубли"],
                                                            total_price["копейки"])
    return string_result


def parse_price(price_string):
    lst = price_string.split(" ")
    price = dict()
    price["рубли"] = int(lst[0])
    price["копейки"] = int(lst[2])
    return price


p1 = "3 рубля 20 копеек"
p3 = "3 рубля 20 копеек"
p5 = "3 рубля 20 копеек"
print(calculate_total_price(p1, p3, p5))
