a = int(input('Введите сторону A: '))
b = int(input('Введите сторону B: '))
c = int(input('Введите сторону C: '))
p = (a + b + c)
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

if (a + b) > c and (b + c) > a and (c + a) > b:
    print('Площадь треугольника: ', s)
else:
    print('неверные данные')
