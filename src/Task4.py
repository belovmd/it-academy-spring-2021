def count_upper_and_lower(string):
    upper = 0
    lower = 0
    for letter in string:
        ascii_num = ord(letter)
        if ascii_num > 64 and ascii_num < 91:
            upper += 1
            print(letter)
        elif ascii_num > 96 and ascii_num < 123:
            lower += 1
    return f"String contain {upper} capital and {lower} lowercase letters"


# TEST
print(count_upper_and_lower('CounT    LoweR    ANd UPper LetTerS!      '))
