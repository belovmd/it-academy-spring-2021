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
    sum = 0
    for num in n:
        sum += int(num)
    counter += 1
    return digital_root(sum, counter)


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
