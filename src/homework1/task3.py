# Пользователь вводит трехзначное число. Программа должна сложить цифры, из которых состоит это число

d = int(input('Введите трехзначное число : '))

if (d < 100) or (d > 999):
    print('Не трехзначное число!!!')
else:
    hundred = d // 100
    dozens = (d-hundred*100) // 10
    units = d % 10

    print('Сумма цифр = ', hundred+dozens+units)
