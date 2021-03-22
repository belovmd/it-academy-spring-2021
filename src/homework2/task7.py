def check_triangle_side(a, b, c):
    if a + b < c:
        return False
    elif a + c < b:
        return False
    elif b + c < a:
        return False
    return True


def calculate_square(a, b, c):
    state = check_triangle_side(a, b, c)
    if not state:
        print("Current triangle does not exist")
        return 0
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c))**(1 / 2)


print("Square {:.4f}".format(calculate_square(3, 10, 9)))
