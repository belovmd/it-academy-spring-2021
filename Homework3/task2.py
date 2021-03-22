# List practice
# 1. Используйте генератор списков чтобы получить следующий:
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
# 2. Используйте на предыдущий список slice чтобы получить следующий:
# ['ab', 'ad', 'bc'].
# 3. Используйте генератор списков чтобы получить следующий
# ['1a', '2a', '3a', '4a'].
# 4. Одной строкой удалите элемент '2a' из прошлого списка и напечатайте его.
# 5. Скопируйте список и добавьте в него элемент '2a'
# так чтобы в исходном списке этого элемента не было.
mystr = 'abcd'

count_number = 0
count_str = 0
lst = ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
lst_new = []
lst_new_3 = []
lst_new_4 = []
lst_new_5 = []
# 1. Используйте генератор списков чтобы получить следующий:
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
while count_number < len(mystr):
    while count_str < len(mystr):
        total = mystr[count_number] + mystr[count_str]
        if total in lst:
            lst_new.append(total)
        count_str += 1
    count_number += 1
    count_str = 0
print(lst_new)

# 2. Используйте на предыдущий список slice чтобы получить следующий:
# ['ab', 'ad', 'bc'].
print(lst_new[::2])

# 3. Используйте генератор списков чтобы получить следующий
# ['1a', '2a', '3a', '4a']
count_number = 1
while count_number < 5:
    total = str(count_number) + 'a'
    lst_new_3.append(total)
    count_number += 1
print(lst_new_3)

# 4. Одной строкой удалите элемент '2a' из прошлого списка и напечатайте его.
lst_new_3.remove('2a')
print(lst_new_3)

# 5. Скопируйте список и добавьте в него элемент '2a'
# так чтобы в исходном списке этого элемента не было.
lst_new_5 = lst_new_3[::]
lst_new_5.append('2a')
print(lst_new_5)
