def fib_number_calculate(n):
    if n < 0 and isinstance(n, float):
        print("Exception :: wrong number")
        return
    fib_number_1, fib_number_2 = 0, 0
    i = 0
    while i <= n:
        if not i:
            fib_number_1 = 0
            i += 1
        elif i == 1:
            fib_number_2 = 1
            i += 1
        else:
            fib_number_2, fib_number_1 = fib_number_1 + fib_number_2, fib_number_2
            i += 1
    return fib_number_2


for i in range(10):
    print(fib_number_calculate(i), end=" ")
