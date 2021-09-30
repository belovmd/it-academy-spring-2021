# Написать программу которая находит ближайшую степень двойки к
# введенному числу. 10(8), 20(16), 1(1), 13(16)
def num(number):
    degree = -1
    while True:
        degree += 1
        if 2 ** degree <= number < 2 ** (degree+1):
            first_number = number % (2**degree)
            sec_number = (2**(degree + 1)) % number
            if first_number > sec_number:
                return "{}({})".format(number, 2**(degree + 1))
            elif first_number == sec_number and number != 1:
                return "{}({},{})".format(number, 2**degree, 2**(degree + 1))
            else:
                return "{}({})".format(number, 2**degree)


print(num(265))
