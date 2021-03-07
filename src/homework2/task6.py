a = int(input('Введите число'))
d = a
b = 0

while a > 0:
    c = a % 10
    a = a // 10
    b = b * 10
    b = b + c

if (d - b) == 0:
    print('палиндром')
else:
    print('No!')
