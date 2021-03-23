# Условие:
# Try to find out how many zeros a given number has at the end.
# Input: A positive Int
# Output: An Int.
# Ссылка:
#  https://py.checkio.org/mission/end-zeros/solve/

def end_zeros(num: int) -> int:
    number_of_zeros = 0
    num = str(num)
    num = num[::-1]
    for one_num in num:
        if one_num != '0':
            break
        number_of_zeros += 1
    return number_of_zeros


print(end_zeros(23783000))
