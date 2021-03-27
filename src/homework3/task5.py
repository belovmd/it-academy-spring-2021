list_ = [5, 2, 5, 6, 7, 3, 1, 1, 5]
list_set = []
for number in list_:
    if number not in list_set:
        list_set.append(number)
print(*list_set)
