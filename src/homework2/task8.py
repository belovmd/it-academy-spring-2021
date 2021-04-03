import re


"""Write a function, which takes a non-negative integer (seconds) as input and returns

the time in a human-readable format (HH:MM:SS)
HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""

# 5 kyu task in www.codewars.com


def make_readable(seconds):
    # make function more easier
    hours, seconds = divmod(seconds, 60 ** 2)
    minutes, seconds = divmod(seconds, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)


# testing
print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))


""" Convert string to camel case

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""

# 6 kyu task


def to_camel_case(text):
    if text:
        text = re.sub(r"[-_]", " ", text)
        text = text.split()
        for word in text[1:]:
            text[text.index(word)] = word.capitalize()
        return ''.join(text)
    else:
        return ''


# testing
print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))


""" 6 kyu Find the unique number

There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([1, 1, 1, 2, 1, 1]) == 2
find_uniq([0, 0, 0.55, 0, 0]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance."""


def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


print(find_uniq([1, 1, 1, 2, 1, 1]))
print(find_uniq([0, 0, 0.55, 0, 0]))

# This is link of my account: https://www.codewars.com/users/Talion90/completed_solutions
