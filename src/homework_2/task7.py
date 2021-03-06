print("Проверка треугольника")
a = float(input("Сторона a ="))
b = float(input("Сторона b="))
c = float(input("Сторона c="))
semi_perimeter = (a + b + c) / 2
S = (semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))**.5

if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
    print("Площадь треугольника", S)
else:
    print("Треугольников с такими сторонами не бывает")
