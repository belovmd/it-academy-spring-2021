# task7

# Даны два натуральных числа.
# Вычислите их наибольший общий делитель при помощи алгоритма Евклида.

number_up, number_down = int(input()), int(input())
if number_up < number_down:
    number_up, number_down = number_down, number_up
while True:
    remainder_of_the_division = number_up % number_down
    number_up, number_down = number_down, remainder_of_the_division
    if not remainder_of_the_division:
        break
print('НОД =', number_up)
if number_down == number_up:
    print('НОД =', number_up)
