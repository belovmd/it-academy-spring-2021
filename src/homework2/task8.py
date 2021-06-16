"""
Task 1

You will be given an array of numbers.
You have to sort the odd numbers in ascending order
while leaving the even numbers at their original positions.
"""


def sort_array(source_arr):
    for i in range(0, len(source_arr) - 1):
        if source_arr[i] % 2 == 0:
            continue
        for j in range(i + 1, len(source_arr)):
            if source_arr[j] % 2 == 0:
                continue
            if source_arr[i] > source_arr[j]:
                source_arr[i], source_arr[j] = source_arr[j], source_arr[i]
    return source_arr


"""
Task 2

The main idea is to count all the occurring characters in a string.
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
What if the string is empty? Then the result should be empty object literal,
{}.
"""


def count(string):
    result = {}
    for letter in string:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


"""
Task 3

Digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n.
If that value has more than one digit,
continue reducing in this way until a single-digit number is produced.
The input will be a non-negative integer.
942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
"""


def digital_root(n, counter=0):
    n = str(n)
    if len(n) <= 1 and counter > 0:
        return int(n)
    sum_ = 0
    for num in n:
        sum_ += int(num)
    counter += 1
    return digital_root(sum_, counter)


"""
Task 4

Given an array (arr) as an argument complete the function countSmileys
that should return the total number of smiling faces.
Rules for a smiling face:
Each smiley face must contain a valid pair of eyes.
Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to.
Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth
that should be marked with either ) or D
No additional characters are allowed except for those mentioned.
"""


def count_smileys(arr):
    valid_smile = [":)", ";)", ":D", ";D",
                   ":-)", ";-)", ":-D", ";-D",
                   ":~)", ";~)", ":~D", ";~D"]
    return len([el for el in arr if el in valid_smile])


"""
Task 5

Implement a function that receives two IPv4 addresses,
and returns the number of addresses between them
(including the first one, excluding the last one).
All inputs will be valid IPv4 addresses in the form of strings.
The last address will always be greater than the first one.
"""


def ips_between(start, end):
    st, e = start.split('.'), end.split('.')
    result = 0
    max_ips = 256

    for degree in range(4):
        result += (int(e[degree]) - int(st[degree])) * max_ips ** (3 - degree)

    return result


"""
Task 6

Write a function that accepts a square matrix (N x N 2D array)
and returns the determinant of the matrix.
"""


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    result = 0
    for y in range(len(matrix)):
        minor = [matrix[x][:y] + matrix[x][y + 1:] for x in range(1, len(matrix))]
        mult = -1 if y % 2 else 1
        result += matrix[0][y] * mult * determinant(minor)

    return result


"""
Task 7

The aim of this kata is to split a given
string into different strings of equal size
(note size of strings is passed to the method)
"""


def split_in_parts(s, part_length):
    result = ''
    str_to_split = s
    while len(str_to_split):
        result += str_to_split[:part_length] + ' '
        str_to_split = str_to_split[part_length:]

    return result.rstrip()


"""
Task 8

Your job is to write a function which increments a string, to create a new string.
If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
"""


def increment_string(strng):
    for i in range(1, len(strng)):
        if strng[-i].isnumeric():
            if int(strng[-i]) < 9:
                return strng[:-i] + str(int(strng[-i:]) + 1)
        else:
            if strng[-i + 1] == '9':
                return strng[:-i + 1] + str(int(strng[-i + 1:]) + 1)
    return str(int(strng) + 1) if strng.isnumeric() else strng + '1'


"""
Task 9

Pete likes to bake some cakes.
He has some recipes and ingredients.
Unfortunately he is not good in maths.
Can you help him to find out, how many cakes he could bake considering his recipes?
Write a function cakes(),
which takes the recipe (object) and the available ingredients (also an object)
and returns the maximum number of cakes Pete can bake (integer).
For simplicity there are no units for the amounts
(e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200).
Ingredients that are not present in the objects, can be considered as 0.
"""


def cakes(recipe, available):
    min_ = None
    for ingredient in recipe:
        if ingredient not in available:
            return 0
        possible_quantity = available[ingredient] // recipe[ingredient]
        if not min_ or possible_quantity < min_:
            min_ = possible_quantity
    return min_
