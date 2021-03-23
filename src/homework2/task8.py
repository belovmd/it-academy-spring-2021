"""
6 kyu
Vasya - Clerk

The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing
in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly
in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment.
Otherwise return NO.
"""


def tickets(people):
    d25 = 0
    d50 = 0
    d100 = 0
    for every in people:
        if every == 25:
            d25 += 1
        elif every == 50:
            if d25 >= 1:
                d50 += 1
                d25 -= 1
            else:
                return "NO"
        else:
            if d50 >= 1 and d25 >= 1:
                d100 += 1
                d50 -= 1
                d25 -= 1
            elif d25 >= 3:
                d100 += 1
                d25 -= 3
            else:
                return "NO"
    return "YES"


"""
6 kyu
Create Phone Number

Write a function that accepts an array of 10 integers (between 0 and 9),
that returns a string of those numbers in the form of a phone number.

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
"""


def create_phone_number(n):
    template = "({}{}{}) {}{}{}-{}{}{}{}"
    return template.format(*n)


"""
6 kyu
Sum of Digits / Digital Root

Given n, take the sum of the digits of n. If that value has more than one digit,
continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
"""


def digital_root(n):
    summa = 0

    if n > 9:
        while n > 0:
            digit = n % 10
            summa += digit
            n = n // 10

            if summa > 9:
                while summa > 0:
                    digit = summa % 10
                    n += digit
                    summa = summa // 10

    if summa == 0:
        return n
    else:
        return summa


"""
6 kyu
Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Note: If the number is a multiple of both 3 and 5, only count it once.
Also, if a number is negative, return 0(for languages that do have them)

"""


def solution(number):
    if number < 0:
        print(0)
    else:
        summa = 0
        for element in range(number):
            if element % 3 == 0 or element % 5 == 0:
                summa += element
        return summa

# Короткое решение:
# def solution(number):
#     if number < 0:
#         print(0)
#     else:
#         return sum(element for element in range(number) if element % 3 == 0 or element % 5 == 0)


"""
8 kyu
Convert a string to an array
Write a function to split a string and convert it into an array of words.
"""


def string_to_array(s):
    return s.split(' ')
