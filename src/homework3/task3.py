# Tuple practice
# 1. Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
# 2. Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
# 3. Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
# 4. Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы
# последовательно выводились значения 1, 2, 3.
# Убедитесь что len() исходного кортежа возвращает 1.


tpl = tuple(['a', 'b', 'c'])
lst = list(('a', 'b', 'c'))
a, b, c = 'a', 2, 'python'
t = ([1, 2, 3],)

print(tpl)
print(lst)
print(a, b, c)
print(len(t))
print(t)
