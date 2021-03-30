"""Homework 3 - Task5"""

# Find unique elements in list
lst_ = [3, 1, 2, 3, 1, 3, 3, 4, "test", "test", "unique"]

for index in lst_:
    if lst_.count(index) == 1:
        print(index)
