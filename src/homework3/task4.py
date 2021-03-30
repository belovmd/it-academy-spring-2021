"""Homework 3 - Task4"""

# Find number or pairs
str_ = "1 1 2 2 2 3 3 3 3 4 4 4 4 5"

lst_ = [int(x) for x in str_.split()]
dct_ = {i: (lst_.count(i) * (lst_.count(i) - 1) // 2) for i in lst_}
print(dct_)
