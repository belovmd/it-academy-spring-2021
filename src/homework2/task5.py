n = int(input('Введите n : '))

if n == 1 or n == 2:
    print('Ответ : ', 1)
else:
    f1 = 1
    f2 = 1
    i = 2
    while i < n:
        fib = f1 + f2
        f1 = f2
        f2 = fib
        i = i + 1
    print('Ответ : ', fib)
