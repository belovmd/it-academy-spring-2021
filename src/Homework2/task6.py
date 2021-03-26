seed = int(input())
check_number = seed
num_finish = 0
while seed > 0:
    num_finish = (10 * num_finish) + seed % 10
    seed //= 10
if check_number == num_finish:
    print('Палиндром')
else:
    print('Число не является Палиндромом')
