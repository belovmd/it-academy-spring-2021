def isPalindrome(num):
    value_to_divide = num
    value_to_check = 0

    while value_to_divide > 0:
        value_to_check = value_to_check * 10 + (value_to_divide % 10)
        value_to_divide //= 10

    return value_to_check == num
