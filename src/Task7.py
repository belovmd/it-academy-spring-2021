def is_triangle(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        p = (a + b + c) / 2
        s_squared = p * (p - a) + (p - b) * (p - c)
        s = s_squared ** 0.5
        print(f"Площадь треугольника равна {s}")
    else:
        print("Перепроверьте данные")
