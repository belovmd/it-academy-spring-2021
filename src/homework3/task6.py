lst_1 = [1, 5, 6, 0, 4, 0, 7, 0]
num_0 = lst_1.count(0)
while True:
    lst_1.remove(0)
    if lst_1.count(0) == 0:
        lst_1 = lst_1 + [0] * num_0
        break
print(lst_1)
