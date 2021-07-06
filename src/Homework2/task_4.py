""""
Homework2 (task_4)
Посчитать колличество символов верхнего и нижнего регистра


"""

text = str(input('Введите строку: ').replace(' ', ''))

print('Upper', sum(map(str.isupper, text)))
print('Lower', sum(map(str.islower, text)))
