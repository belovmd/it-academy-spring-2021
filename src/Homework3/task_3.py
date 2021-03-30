# Task 3. Tuple practice:
# 1. Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
# 2. Создайте кортеж ('a', 'b', 'c'), И сделайте из него список.
# 3 Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
# 4. Создайте кортеж из одного элемента, чтобы при итерировании по этому
# элементы последовательно выводились значения 1, 2, 3. Убедитесь что len()
# исходного кортежа возвращает 1.

list_to_tuple = tuple(["a", "b", "c"])
print("Tuple:", list_to_tuple)

tuple_to_list = list(list_to_tuple)
print("List:", tuple_to_list)

a, b, c = "a", 2, "python"
tuple_with_123 = ([1, 2, 3], )
print("len(tuple_with_123):", len(tuple_with_123))

for element in tuple_with_123:
    [print(num) for num in element]
