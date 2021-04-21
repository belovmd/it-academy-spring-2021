#2. List practice
#2.1. Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
#2.2. Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
#2.3. Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
#2.4. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
#2.5. Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента не было.


print('task: 2.1')
task_2_1 = [a + b for a in "ab" for b in "bcd"]
print(task_2_1)


print('task: 2.2')
task_2_2 = task_2_1[::2]
print(task_2_2)


print('task: 2.3')
numbers = list(range(1, 5))
letters = ["a"]
task_2_3 = [str(number) + letter for number in numbers for letter in letters]
print(task_2_3)


print('task: 2.4')
task_2_3.remove('2a')
print(task_2_3)


print('task: 2.5')
task_2_5 = task_2_3.copy()
task_2_5.insert(1, '2a')
print(task_2_5)