for num in range(1, 101):
    if not num % 3 and not num % 5:
        print('FizzBuzz')
    elif not num % 3:
        print('Fizz')
    elif not num % 5:
        print('Buzz')
    else:
        print(num)
