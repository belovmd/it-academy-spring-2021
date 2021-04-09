# Bob is preparing to pass IQ test. The most frequent task in this test is to
# find out which one of the given numbers differs from the others. Bob observed
# that one number usually differs from the others in evenness. Help Bob — to check
# his answers, he needs a program that among the given numbers finds one that is
# different in evenness, and return a position of this number.
# ! Keep in mind that your task is to help Bob solve a real IQ test, which means
# indexes of the elements start from 1 (not 0)

iq_test = "2 4 7 8 10"
lst = list(iq_test.split())
lst1 = [num for num in lst if int(num) % 2]
if len(lst1) == 1:
    n = lst1[0]
    index = lst.index(n) + 1
    print(index)
else:
    lst2 = [num for num in lst if not int(num) % 2]
    n = lst2[0]
    index = lst.index(n) + 1
    print(index)


# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is
# an isogram. Assume the empty string is an isogram. Ignore letter case.

str_ = "Isogram"
set_ = set(str_.lower())
if len(str_) == len(set_):
    print("This is a word is isogram")
