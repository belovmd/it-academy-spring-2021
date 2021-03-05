def count_total_amount(ruble, kopeck, quantity_of_goods):
    if ruble < 0 or kopeck < 0 or quantity_of_goods < 0:
        return "Перепроверьте данные"
    total_rub_amount = ruble * quantity_of_goods
    total_kop_amount = kopeck * quantity_of_goods
    while total_kop_amount > 100:
        total_rub_amount += 1
        total_kop_amount -= 100
    return f"Общая цена {total_rub_amount} рублей {total_kop_amount} копеек"


# TEST
print(count_total_amount(3, 20, 3))
print(count_total_amount(-3, 20, 3))
