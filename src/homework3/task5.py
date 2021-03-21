import random

random.seed(505011)


lst_ = [random.randint(1, 30) for i in range(1, 25)]
print("Исходный список:", *lst_)
unique_elements = [elem for elem in lst_ if lst_.count(elem) == 1]
print("Уникальные элементы:", *unique_elements)
