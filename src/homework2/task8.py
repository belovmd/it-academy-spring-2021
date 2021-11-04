# You live in the city of Cartesia where all roads are laid out in a perfect grid.
# You arrived ten minutes too early to an appointment, so you decided to take the
# opportunity to go for a short walk. The city provides its citizens with a Walk
# Generating App on their phones -- everytime you press the button it sends you an
# array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']).
# You always walk only a single block for each letter (direction) and you know it takes
# you one minute to traverse one city block, so create a function that will return true
# if the walk the app gives you will take you exactly ten minutes (you don't want to be early
# or late!) and will, of course, return you to your starting point. Return false otherwise.
# Note: you will always receive a valid array containing a random assortment of direction
# letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a
# walk, that's standing still!)

def is_valid_walk(walk):
    letter_n = walk.count('n')
    letter_s = walk.count('s')
    letter_e = walk.count('e')
    letter_w = walk.count('w')
    north_walk = (letter_n - letter_s)
    west_walk = (letter_e - letter_w)
    if len(walk) == 10 and not north_walk and not west_walk:
        return True
    else:
        return False

# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result
# in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255.
# Any values that fall out of that range must be rounded to the closest valid value.
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.


def rgb(r, g, b):
    lst = [r, g, b]
    for i in range(3):
        if lst[i] < 0:
            lst[i] = 0
        elif lst[i] > 255:
            lst[i] = 255

    return "{:02X}{:02X}{:02X}".format(lst[0], lst[1], lst[2])


# Greed is a dice game played with five six-sided dice. Your mission, should you choose to
# accept it, is to score a throw according to these rules. You will always be given an
# array with five six-sided dice values.
#
#  Three 1's => 1000 points
#  Three 6's =>  600 points
#  Three 5's =>  500 points
#  Three 4's =>  400 points
#  Three 3's =>  300 points
#  Three 2's =>  200 points
#  One   1   =>  100 points
#  One   5   =>   50 point
# A single die can only be counted once in each roll. For example, a given
# "5" can only count as part of a triplet (contributing to the 500 points)
# or as a single 50 points, but not both in the same roll.

def score(dice):
    points = 0
    if dice.count(1) < 3:
        points = points + dice.count(1) * 100
    elif dice.count(1) >= 3:
        points = points + 1000 + (dice.count(1) % 3) * 100

    if dice.count(5) < 3:
        points = points + dice.count(5) * 50
    elif dice.count(5) >= 3:
        points = points + 500 + (dice.count(1) % 3) * 50

    if dice.count(2) >= 3:
        points = points + 200

    if dice.count(3) >= 3:
        points = points + 300

    if dice.count(4) >= 3:
        points = points + 400

    if dice.count(6) >= 3:
        points = points + 600

    return points


# In this kata we want to convert a string into an integer.
# The strings simply represent the numbers in words.
# Examples:
# "one" => 1
# "twenty" => 20
# "two hundred forty-six" => 246
# "seven hundred eighty-three thousand nine hundred and nineteen" => 783919
# Additional Notes:
# The minimum number is "zero" (inclusively)
# The maximum number, which must be supported is 1 million (inclusively)
# The "and" in e.g. "one hundred and twenty-four" is optional, in some cases
# it's present and in others it's not
# All tested numbers are valid, you don't need to validate them


def parse_int(string):
    dct = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11,
        'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
        'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30,
        'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,
        'hundred': 100, 'thousand': 1000, 'million': 1000000
    }
    st = string.split(' ')
    clear_string = []
    numbers = []
    number = 0
    for i in st:
        str_1 = i.split('-')
        clear_string.extend(str_1)

    for i in clear_string:
        if i != "hundred":
            numbers.append(dct.get(i, 0))
        elif i == 'hundred':
            n = numbers.pop()
            numbers.append(n * dct.get(i))

    for i in numbers:
        if i == 1000:
            number = number * 1000
        elif i == 1000000:
            number = number * 1000000
        else:
            number += i

    return number

# Create a function that takes a positive integer and returns the next bigger number
# that can be formed by rearranging its digits. For example:
#
# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071
# nextBigger(num: 12)   // returns 21
# nextBigger(num: 513)  // returns 531
# nextBigger(num: 2017) // returns 2071
# If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):
#
# 9 ==> -1
# 111 ==> -1
# 531 ==> -1


def next_bigger(n):
    lst_ = list(str(n))
    lst_end = []
    for i in range(len(lst_) - 1, 0, -1):
        if lst_[i] > lst_[i - 1]:
            tail = lst_[i::]
            tail.append(lst_[i - 1])
            tail.sort()
            a = tail.pop((tail.index(lst_[i-1]) + tail.count(lst_[i-1])))
            tail.insert(0, a)
            if i == 1:
                lst_end.extend(tail)
            else:
                nose = lst_[:i - 1:1]
                lst_end.extend(nose)
                lst_end.extend(tail)
            break

    if not lst_end:
        return -1
    else:
        return int(''.join(lst_end))
