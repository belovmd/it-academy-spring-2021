list_ = [0, 2, 5, 0, 7, 0, 1, 1, 0]
number_of_zeros = 0
for index_list in range(len(list_)):
    if list_[index_list]:
        print(list_[index_list], end=" ")
    else:
        number_of_zeros += 1
for _ in range(number_of_zeros):
    print(0, end=" ")
