# Bob is preparing to pass IQ test. The most frequent task in this test is to
# find out which one of the given numbers differs from the others. Bob observed
# that one number usually differs from the others in evenness. Help Bob — to check
# his answers, he needs a program that among the given numbers finds one that is
# different in evenness, and return a position of this number.
# ! Keep in mind that your task is to help Bob solve a real IQ test, which means
# indexes of the elements start from 1 (not 0)

iq_test = "2 4 7 8 10"
number = 3
str_ = iq_test.split()
for num in str_:
    if number % 2:
        if int(num) % 2:
            print(num)
    elif not number % 2:
        if not int(num) % 2:
            print(num)


# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is
# an isogram. Assume the empty string is an isogram. Ignore letter case.

str_ = "isIsogram"
other_str = str_.lower()
lst = []
for i in other_str:
    if i not in lst:
        lst.append(i)
if len(other_str) == 0 or len(other_str) == len(lst):
    print("true")
else:
    print("false")
