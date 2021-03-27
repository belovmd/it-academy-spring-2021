list_ = ['a', 'b', 'c']
tuple_ = tuple(list_)
tuple_2 = ('a', 'b', 'c')
list_2 = list(tuple_2)
a, b, c = 'a', 2, 'python'

tuple_3 = ([1, 2, 3],)
for i in tuple_3[0]:
    print(i, end=' ')
print()
print(len(tuple_3))
