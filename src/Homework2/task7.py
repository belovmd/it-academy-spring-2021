a, b, c = int(input()), int(input()), int(input())
if a + b > c and b + c > a and a + c > b:
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c))**0.5
    print('Треугольник существует, его площадь равна {} у.е.'.format(s))
else:
    print('Неверные данные')
