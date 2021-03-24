"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples
of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once.
Also, if a number is negative, return 0(for languages that do have them)

Courtesy of projecteuler.net
"""
first_digit = 3
second_digit = 5
number = 100
result_sum = 0
for index in range(1, number):
    if index % first_digit == 0 or index % second_digit == 0:
        result_sum += index
print(result_sum)
