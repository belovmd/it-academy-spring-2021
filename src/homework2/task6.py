"""Homework2 - task6

Определите, является ли число палиндромом (читается слева
направо и справа налево одинаково).  Число положительное целое,
произвольной длины. Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)
"""

input_num = int(input("Input number: "))
str_num = input_num
rev_num = 0

while str_num:
    rev_num, str_num = rev_num * 10 + str_num % 10, str_num // 10

if input_num == rev_num:
    print("Number is palindrome!")
else:
    print("Number is NOT palindrome!")
