def homework3_task1():
    def fizz_buzz(input_num=100):
        for i in range(1, input_num + 1):
            str_ = ""
            if not i % 3:
                str_ += "Fizz"
            if not i % 5:
                str_ += "Buzz"
            print(str_ if str_ else i)

    fizz_buzz()


def homework3_task2():

    a = [i + j for i in 'ab' for j in 'bcd']
    print(a)
    print(a[::2])

    b = [i + j for i in '1234' for j in 'a']
    print(b)
    print(b.pop(1))

    c = b.copy()
    c.append('2a')
    print(b, c)


def homework3_task3():

    tpl = tuple(['a', 'b', 'c'])
    lst = list(('a', 'b', 'c'))
    a, b, c = 'a', 2, 'python'
    t = ([1, 2, 3],)

    print(tpl)
    print(lst)
    print(a, b, c)
    print(len(t))
    print(t)


def homework3_task4():

    def count_pairs(str_):
        dict_ = {}

        for elem in str_.split(' '):
            if elem not in dict_:
                dict_[elem] = 0
            dict_[elem] += 1

        for elem in dict_:
            pairs = sum(range(dict_[elem]))
            if pairs > 0:
                print("Element {} has {} pair(s)".format(elem, pairs))

    print(count_pairs("1 1 2 5 2 7 9 10 10 1 1 1"))


def homework3_task5():

    lst = [1, 5, 2, 6, 2, 1, 7]
    [print(elem) for elem in lst if lst.count(elem) == 1]


def homework3_task6():

    lst = [1, 2, 15, 0, 0, 3, 17, 4, 19, 0, 7]

    index = num_of_changes = 0

    while num_of_changes + index <= len(lst) - num_of_changes:
        if lst[index]:
            index += 1
        else:
            lst.append(lst.pop(index))
            num_of_changes += 1

    print(lst)
