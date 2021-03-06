# Check your number on polindromphism
# Create many vars for work
my_number = int(input("Enter a number: "))
new_number = my_number
for_comp_number = my_number
rev_number = 0
count_dec = 0

# Найдем разряность числа
while new_number > 1:
    count_dec += 1
    new_number = new_number / 10

# Разворачиваем число
while count_dec != 0:
    ost = my_number % 10
    rev_number += ost
    rev_number = rev_number * 10
    my_number = (my_number - ost) / 10
    count_dec -= 1
rev_number = rev_number / 10

if for_comp_number == rev_number:
    print("This number is polindrom")
else:
    print("No no no")
