rub = int(input("Введите количество рублей: "))
cop = int(input("Введите количество копеек: ")) / 100
numb = int(input("Введите количество товара: "))
price = rub + cop
all_cost = str(price * numb)
itog_rub, itog_cop = all_cost.split(".")
print("Итоговая цена составляет {0} рублей {1} копеек".format(itog_rub, itog_cop))
