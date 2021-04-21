#6. Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
# Число положительное целое, произвольной длины.
# Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще)


# 1 вариант (для цифр)
data = int(121)
print ("Entered data = ", data)
reverse_number = 0
number = 0
while (data // (10**number) != 0):
  reverse_number = (reverse_number * 10) + (data // (10** number) % 10)
  number += 1
if data == reverse_number:
  print("Entered data is palindrome")
else:
  print("Entered data is not palindrome")


# 2 вариант
info = '''abcba'''
print ("Entered info = ", info)
if info[:] == info[-1::-1]:
  print("Entered info is palindrome")
else:
  print("Entered info is not palindrome")