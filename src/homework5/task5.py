# Task 5 — Написать программу которая находит ближайшую степень двойки к
# введенному числу. 10(8), 20(16), 1(1), 13(16)

def closer_value(num):
    base, exponent = 2, 0
    while num > base ** exponent:
        exponent += 1

    if num - base ** (exponent - 1) <= base ** exponent - num:
        print("Value of closer exponentiation", base ** (exponent - 1))
    else:
        print("Value of closer exponentiation", base ** exponent)


closer_value(10)
closer_value(20)
closer_value(1)
closer_value(13)
