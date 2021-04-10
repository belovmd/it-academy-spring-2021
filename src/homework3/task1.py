# FizzBuzz
# Напишите программу, которая печатает цифры от 1 до 100,
# но вместо чисел, кратных 3 пишет Fizz,
# вместо чисел кратный 5 пишет Buzz,
# а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz


def fizz_buzz(input_num=100):
    for i in range(1, input_num + 1):
        str_ = ""
        if not i % 3:
            str_ += "Fizz"
        if not i % 5:
            str_ += "Buzz"
        print(str_ if str_ else i)


fizz_buzz()
