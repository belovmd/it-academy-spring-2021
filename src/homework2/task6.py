num = int(input('Введите число : '))

if num < 10:
    print('Однозначное число!!!')
else:
    n = num
    rev_n = 0
    while n > 0:
        units = n % 10
        rev_n = rev_n * 10 + units
        n = n // 10

    if num == rev_n:
        print('Палиндром')
    else:
        print('Не палиндром')
