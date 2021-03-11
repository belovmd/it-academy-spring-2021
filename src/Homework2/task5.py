number_fib = int(input('Введите номер числа Фибоначчи: '))
count = 0
number_first = 0
number_second = 1

# try to find number with for-loop
for number in range(number_fib - 1):
    count = number_first + number_second
    number_second = number_first
    number_first = count
print(count)
