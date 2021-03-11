import re


"""Write a function, which takes a non-negative integer (seconds) as input and returns

the time in a human-readable format (HH:MM:SS)
HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures."""

# 5 kyu task in www.codewars.com


def make_readable(seconds):
    if seconds > 3599:
        hours_ = int(seconds // 3600)
        minutes_ = int(((seconds / 3600 - hours_) * 60) // 1)
        seconds_ = int(seconds - hours_ * 3600 - minutes_ * 60)
        if seconds_ == 60:
            minutes_ += 1
            seconds_ = ''
    elif seconds > 59:
        hours_ = ''
        minutes_ = int(seconds // 60)
        seconds_ = int((seconds / 60 - minutes_) * 60)
    else:
        hours_ = ''
        minutes_ = ''
        seconds_ = seconds
    if len(str(hours_)) == 2:
        hours = str(hours_)
    elif len(str(hours_)) == 1:
        hours = '0' + str(hours_)
    else:
        hours = '00'
    if len(str(minutes_)) == 2:
        minutes = str(minutes_)
    elif len(str(minutes_)) == 1:
        minutes = '0' + str(minutes_)
    else:
        minutes = '00'
    if len(str(seconds_)) == 2:
        sec = str(seconds_)
    elif len(str(seconds_)) == 1:
        sec = '0' + str(seconds_)
    else:
        sec = '00'
    return "{0}:{1}:{2}".format(hours, minutes, sec)


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


""" 6 kyu Find the unique number

There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance."""


def find_uniq(arr):
    n = 0
    n_last = 0
    n_next = 0
    while n_last == n_next:
        if arr[0] != arr[1] and arr[0] != arr[2]:
            return arr[0]
        else:
            n_last = arr[n]
            n_next = arr[n + 1]
            n += 1
    return n_next


# This is link of my account: https://www.codewars.com/users/Talion90/completed_solutions
