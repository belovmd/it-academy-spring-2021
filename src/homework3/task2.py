# Task 2 — list practice:
# 1. Получение ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'] через генератор списков,
# 2. Использование slice для получения ['ab', 'ad', 'bc'],
# 3. Получение ['1a', '2a', '3a', '4a'] с помощью генератора списков,
# 4. Удаление элемента '2a' одной строков из прошлого списка и его печать,
# 5. Копирование списка и добавление элемента '2a' так, чтобы в исходном списке
# этого элемента не было.

first_list = [el1 + el2 for el1 in "ab" for el2 in "bcd"]
print("First list:", first_list)

second_list = first_list[::2]
print("Second list:", second_list)

third_list = [str(number) + "a" for number in "1234"]
print("Third list:", third_list)

print("Extracted element:", third_list.pop(third_list.index("2a")))

forth_list = third_list.copy()
forth_list.append("2a")
print("Third list without '2a':", third_list)
print("Copy of the third list with '2a' appended:", forth_list)
