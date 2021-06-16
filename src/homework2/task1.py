def count_total_amount(ruble, kopeck, quantity_of_goods):
    total_rub_amount = ruble * quantity_of_goods
    total_kop_amount = kopeck * quantity_of_goods
    while total_kop_amount > 100:
        total_rub_amount += 1
        total_kop_amount -= 100
    return f"Общая цена {total_rub_amount} рублей {total_kop_amount} копеек"


print(count_total_amount(3, 20, 3))
