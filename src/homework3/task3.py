"""Homework 3 - Task3

Tuple practice
Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
Создайте кортеж из одного элемента, чтобы при итерировании по этому
элементы последовательно выводились значения 1, 2, 3. Убедитесь что len()
исходного кортежа возвращает 1.
"""

# 1 Create tuple from list
lst_ = ["a", "b", "c"]
tpl_ = tuple(lst_)
print(tpl_, type(tpl_))

# 2 Create list from tuple
lst_2 = list(tpl_)
print(lst_2, type(lst_2))

# 3 One string assignment
a, b, c = "a", 2, "python"
print(a, b, c)

# 4 One element tuple
tpl_2 = ([1, 2, 3],)
for index in tpl_2[0]:
    print(index)
print(len(tpl_2))
