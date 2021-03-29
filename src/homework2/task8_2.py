"""Homework2 - task8_2"""

"""
Numbers ending with zeros are boring.
They might be fun in your world, but not here.
Get rid of them. Only the ending ones.
1450 -> 145;     960000 -> 96;    1050 -> 105;       -1050 -> -105;
Zero alone is fine, don't worry about it. Poor guy anyway
"""

number = 120

if number != 0:
    while not number % 10:
        number = number // 10
print(number)
