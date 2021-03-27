for number in range(1, 101):
    if not number % 3 and not number % 5:
        print('FizzBuzz')
    elif not number % 3:
        print('Fizz')
    elif not number % 5:
        print('Buzz')
    else:
        print(number)
