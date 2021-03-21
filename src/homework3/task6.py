lst_ = [0, 1, 2, 0, 3, 4, 0, 5, 0, 6, 0, 0, 0, 0, 0, 0, 7, 0,
        8, 0, 0, 0, 0, 0, 9, 10, 11, 0, 0, 0, 0, 12, 0, 0, 0]
print("Исходный список:", *lst_)
i = 0
counter = count_null = lst_.count(0)
while counter:
    if not lst_[i]:
        lst_.pop(i)
        lst_.append(0)
        counter -= 1
        continue
    i += 1
print("После перестановки:", *lst_)
