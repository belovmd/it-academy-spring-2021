# Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
# Число положительное целое, произвольной длины. Задача требует работать только с числами
# (без конвертации числа в строку или что-нибудь еще)

number = 100001
n = number
new_number = 0
while n > 0:
    ostatok = n % 10
    new_number = new_number * 10 + ostatok
    n = n // 10
if new_number == number:
    print('polindrom')
else:
    print('not polindrom')
