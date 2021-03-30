"""Homework 3 - Task3"""

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
