for elem in range(1, 101):
    if not elem % 3 and not elem % 5:
        print("FizzBuzz", end=" ")
    elif not elem % 3:
        print("Fizz", end=" ")
    elif not elem % 5:
        print("Buzz", end=" ")
    else:
        print(elem, end=" ")
