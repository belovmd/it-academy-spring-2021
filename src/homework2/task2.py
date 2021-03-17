# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.

string = 'Вводится M рублей и N копеек цена, а также количество S товара ' \
         'Посчитайте общую цену в рублях и копейках за L товаров.'
znaki_prepinaniya = [',', '.', '?', '-', '!']
# убираем знаки препинания
for i in range(0, len(znaki_prepinaniya)):
    string = string.replace(znaki_prepinaniya[i], '')
# возвращаем список строк
new_string = string.split()
max_len, number = 0, 0
for i in range(0, len(new_string)):
    if max_len < len(new_string[i]):
        max_len = len(new_string[i])
        number = i
print('Самое длинное слово:', new_string[number])
