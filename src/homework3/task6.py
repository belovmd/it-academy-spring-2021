"""Homework 3 - Task6"""

# Sort list
lst_ = [3, 1, 0, 2, 3, 0, 1, 3, 0, 3, 4]

lst_.sort(key=bool, reverse=True)
print(lst_)
