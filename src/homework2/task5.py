def fib_number_calculate(n):
    if n < 0 and isinstance(n, float):
        print("Exception :: wrong number")
        return
    fib_number_1 = 0
    fib_number_2 = 0
    result = 0
    i = 0
    while i <= n:
        if i == 0:
            result = fib_number_1 = 0
            i += 1
        elif i == 1:
            result = fib_number_2 = 1
            i += 1
        else:
            result = fib_number_1 + fib_number_2
            fib_number_1 = fib_number_2
            fib_number_2 = result
            i += 1
    return result


for i in range(10):
    print(fib_number_calculate(i), end=" ")
