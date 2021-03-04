# In this mission, you need to create a password verification function.
# The verification condition is:
# the length should be bigger than 6.

def is_acceptable_password(password: str) -> bool:
    if len(password) > 6:
        return True
    else:
        return False


# Complete the solution so that it reverses the string passed into it.

def solution(string):
    return string[::-1]


# Beginner Series #3 Sum of Numbers

def get_sum(a, b):
    if a == b:
        return a
    elif a < b:
        min_ab = a
        max_ab = b
    else:
        min_ab = b
        max_ab = a
    summa = 0
    for i in range(min_ab, max_ab + 1):
        summa = summa + i
    return summa
