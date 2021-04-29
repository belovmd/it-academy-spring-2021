def hmw2_tsk1(rub=5, cop=25, numb=30):
    """Функция считает цену товаров"""
    price = rub + cop / 100
    all_cost = str(price * numb)
    res_rub, res_cop = all_cost.split(".")
    return "Итоговая цена составляет {0} рублей " \
           "{1} копеек".format(res_rub, res_cop)


def hmw2_tsk2(string='Самое длинное слово в этом предложении'):
    """Функция ищет самое длинное слово в строке"""
    formatted_string = "".join(letter for letter in string if
                               letter.isalpha() or
                               letter.isspace() or
                               letter.isdigit())
    lst = formatted_string.split()
    big_word = lst[0]
    for word in lst:
        if len(big_word) < len(word):
            big_word = word
    return "Самое длинное слово в предложении: {}".format(big_word)


def hmw2_tsk3(string="abc cde def"):
    """Функция удаляет повтораяющиеся символы и пробелы"""
    my_string = string.split()
    new_string = ''.join(my_string)
    output_list = []
    for symbol in new_string:
        if symbol not in output_list:
            output_list.append(symbol)
    output_string = ''.join(output_list)
    return output_string
