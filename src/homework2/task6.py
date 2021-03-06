import math


def count_of_digits(num):
    count = 0
    while num:
        count += 1
        num //= 10
    return count


def check_paliandr(chislo):
    count = count_of_digits(chislo)
    state = True
    middle_number = math.ceil(count / 2)
    i = 1
    if count == 1:
        return state
    if not count % 2:
        return False
    while i <= middle_number:
        great_digit = chislo // 10 ** (count - i)
        low_digit = chislo % 10 ** i
        offset_head = great_digit % 10
        offset_tail = low_digit // 10 ** (i - 1)
        if not (offset_tail == offset_head):
            state = False
            break
        i += 1
    return state


chislo1 = 9426341
chislo2 = 32323
chislo3 = 2442
chislo4 = 3
print("{} - {}".format(chislo1, check_paliandr(chislo1)))
print("{} - {}".format(chislo2, check_paliandr(chislo2)))
print("{} - {}".format(chislo3, check_paliandr(chislo3)))
print("{} - {}".format(chislo4, check_paliandr(chislo4)))
