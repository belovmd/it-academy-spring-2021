lst_1 = [1, 2, 3, 2, 5, 1]
for i in range(len(lst_1)):
    if lst_1.count(lst_1[i]) == 1:
        print(lst_1[i])
