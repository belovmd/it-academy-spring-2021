lst_ = [chr1 + chr2 for chr1 in "ab" for chr2 in "bcd"]
print(*lst_)
print(*lst_[::2])
lst_2 = [str(chr1) + 'a' for chr1 in range(1, 5)]
print(*lst_2)
print(lst_2.pop(lst_2.index('2a')))
lst_3 = lst_2.copy()
lst_3.insert(1, '2a')
print(*lst_3)
