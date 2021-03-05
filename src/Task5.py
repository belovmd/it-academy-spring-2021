def find_n_fibonacci(num):
    if num <= 1:
        return 1
    previous = 0
    actual = 1
    for i in range(1, num):
        temp = actual
        actual += previous
        previous = temp
    return actual


print(find_n_fibonacci(8))
