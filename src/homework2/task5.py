n = int(input('Введите n-е число Фибоначи:'))

if 0 < n < 3:
    print(1)
else:
    fib1 = 1
    fib2 = 1
    fib3 = 0
    i = 2
    while i < n:
        fib3 = fib2 + fib1
        fib1 = fib2
        fib2 = fib3
        i += 1
        continue
    print(fib3)
