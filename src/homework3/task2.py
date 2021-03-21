import copy

lst_1 = [smbl_lst_1 + smbl_lst_2 for smbl_lst_1 in ['a', 'b'] for smbl_lst_2 in ['b', 'c', 'd']]
print(lst_1)
lst_2 = [lst_1[num_lst] for num_lst in range(len(lst_1)) if not num_lst % 2]
print(lst_2)
lst_3 = [str(i) + 'a' for i in range(1, 5)]
print(lst_3)
print(lst_3.pop(1))
lst_4 = copy.deepcopy(lst_3)
lst_4.append('2a')
lst_4.sort()
print(lst_4)
