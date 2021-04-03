"""Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).

Число положительное целое, произвольной длины.
Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще)
"""


def check_pol(num):
    # Check your number on polindromphism
    check_num = abs(num)
    reverse_number = 0

    while check_num > 0:
        reverse_number = reverse_number * 10 + check_num % 10
        check_num //= 10

    if abs(num) == reverse_number:
        print("This number is polindrom")
    else:
        print("No no no")


# testing function
check_pol(1221)
check_pol(34567876543)
check_pol(1032098383)
check_pol(11)
check_pol(-121)
check_pol(0)
check_pol(-1232)
