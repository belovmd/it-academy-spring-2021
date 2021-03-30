"""Homework 3 - Task1"""

# Find divisible numbers
first_digit = 3
second_digit = 5

for index in range(1, 101):
    if index % first_digit == 0 and index % second_digit == 0:
        print("FizzBuzz")
    elif index % first_digit == 0:
        print("Fizz")
    elif index % second_digit == 0:
        print("Buzz")
    else:
        print(index)
