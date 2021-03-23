# Условие:
# You are given a string S
# S contains alphanumeric characters only.
# Your task is to sort the string S in the following manner:
#  - All sorted lowercase letters are ahead of uppercase letters.
#  - All sorted uppercase letters are ahead of digits.
#  - All sorted odd digits are ahead of sorted even digits.
# Input Format:
# A single line of input contains the string S.
# Output Format:
# Output the sorted string S.
# Ссылка:
#   https://www.hackerrank.com/challenges/ginorts/problem

S = input()
lst_lower, lst_upper, lst_numbers_even, lst_numbers_odd = [], [], [], []
for i in S:
    if i.islower():
        lst_lower.append(i)
    elif i.isupper():
        lst_upper.append(i)
    else:
        i = int(i)
        if not i % 2:
            lst_numbers_even.append(i)
        else:
            lst_numbers_odd.append(i)
lst_upper.sort()
lst_lower.sort()
lst_numbers_even.sort()
lst_numbers_odd.sort()
print(*lst_lower, *lst_upper, *lst_numbers_odd, *lst_numbers_even, sep='')
