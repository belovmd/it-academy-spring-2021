# Task 7. Даны: три стороны треугольника. Требуется: проверить, действительно
# ли это стороны треугольника. Если стороны определяют треугольник, найти его
# площадь. Если нет, то вывести сообщение о неверных данных.

side_a, side_b, side_c = [int(num) for num in input("Введите 3 числа через "
                                                    "пробел: ").split()]

if side_a + side_b > side_c and side_a + side_c > side_b and \
        side_b + side_c > side_a:
    semi = (side_a + side_b + side_c) / 2

    # semiperimeter is shortened to "semi" because a longer word causes
    # a "line break" error in the next line that I couldn't fix.

    area = (semi * (semi - side_a) * (semi - side_b) * (semi - side_c)) ** 0.5
    print("Площадь треугольника =", area)

else:
    print("Неверные данные")
