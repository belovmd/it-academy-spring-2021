n = int(input("Введите целое число: "))
n2 = n
p = 0

while n2 > 0:
    itr = n2 % 10
    n2 = n2 // 10
    p = p * 10
    p = p + itr

if n == p:
    print('палиндром')

else:
    print('не палиндром')
