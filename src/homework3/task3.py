set_1 = set(['a', 'b', 'c'])
print("set: {}".format(set_1))
list_1 = list(set_1)
print("list: {}".format(list_1))
a, b, c = "a", 2, "python"
print("{a} {b} {c}".format(a=a, b=b, c=c))
set_2 = ([1, 2, 3],)
for elem in set_2[0]:
    print(elem, end=" ")
