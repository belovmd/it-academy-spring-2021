# Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
# Число положительное целое, произвольной длины.
# Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще)
Num = int(input('Введите число'))
start_num = Num
revers_num = 0

while Num > 0:
    remainder = Num % 10
    Num = Num // 10
    revers_num = revers_num * 10
    revers_num = revers_num + remainder

if (start_num - revers_num) == 0:
    print('палиндром')
else:
    print('No!')
