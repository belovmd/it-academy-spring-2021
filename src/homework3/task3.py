# 3. Tuple practice
#   1. Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
#   2.  Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
#   3.  Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
#   4.  Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы последовательно выводились
#   значения 1, 2, 3. Убедитесь что len() исходного кортежа возвращает 1.

print('task: 3.1')
list1 = ['a', 'b', 'c']
list2 = list('abc')
print(list1)
print(list2)
a1 = tuple(list1)
b1 = tuple(list2)
print(a1)
print(b1)


print('task: 3.2')
tuple1 = 'a', 'b', 'c'
print(tuple1)
c1 = list(tuple1)
print(c1)


print('task: 3.3')
a, b, c = 'a', 2, 'python'
# распаковка кортежа
print(a)
print(b)
print(c)


print('task: 3.4')
tuple2 = "a" # ('a')
print(tuple2)
print(len(tuple2))
i = 1
for n in tuple2:
  print(i, n)
  i += 1 # i = i + 1

for j, m in enumerate(tuple2, 1):
  print(j, m)
  j += 1 # j = j + 1