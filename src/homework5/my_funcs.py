# Functions for Task 1


def histogram(lst):
    dict_ = {}
    for item in lst:
        if item in dict_.keys():
            dict_[item] += 1
        else:
            dict_[item] = 1
    for keys in sorted(dict_.keys(), reverse=True):
        print("{}: {}".format(keys, "*" * dict_[keys]))


def stars(num):
    print(num * "*")


def blocks(str_):
    print(len(str_))


def non():
    print("a")

years = [1994, 1972, 1974, 2008, 1957, 1993, 1994, 2003]
ratings = [9.2, 9.2, 9.0, 9.0, 8.9, 8.9, 8.9, 8.9, 8.8, 8.8]

histogram(years)
histogram(ratings)
stars(5)
stars(7)
blocks('name')
blocks('names and years')
