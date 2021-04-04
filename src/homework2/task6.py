"""Homework2 - task6

Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины.
Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще)

"""


n = 75257
if not isinstance(n, int) or n <= 0:
    print('Not valid input number (int from 1 to ... is expected)')
    raise ValueError

source = int(n)
target = 0

while source:
    target, source = (target * 10 + source % 10), (source // 10)

print('Number %s is%s a palindrome' % (n, '' if target == n else ' not'))
