# TASK 8. TASKS FROM CODEWARS

# Task 1 (7 kyu):
# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

def get_count(input_str):
    num_vowels = 0

    for element in input_str:
        if element in ['a', 'o', 'e', 'i', 'u']:
            num_vowels += 1

    return num_vowels


# ____________________________________________________________________________
# Task 2: (7 kyu)
# This time no story, no theory. The examples below show you how to write
# function accum: Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z
# and A..Z.

def accum(s):
    assembling_lst = []
    index_counter = 0

    for element in s.lower():
        assembling_lst.append(element.upper() + (element * index_counter))
        resulting_string = "-".join(assembling_lst)
        index_counter += 1

    return resulting_string


# ____________________________________________________________________________
# Task 3 (7 kyu)
# Trolls are attacking your comment section! A common way to deal with this
# situation is to remove all of the vowels from the trolls' comments,
# neutralizing the threat. Your task is to write a function that takes a string
# and return a new string with all vowels removed. For example, the string
# "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.

def disemvowel(original_str):
    vowels = ['a', 'o', 'u', 'e', 'i']

    for letter in original_str:
        if letter in vowels or letter.lower() in vowels:
            original_str = original_str.replace(letter, "")

    return original_str


# ____________________________________________________________________________
# Task 4 (6 kyu)
# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

def find_it(sequence):

    for number in sequence:
        if sequence.count(number) % 2 != 0:
            break

    return number


# ____________________________________________________________________________
# Task 5 (6 kyu)
# Write a function that takes in a string of one or more words, and returns the
# same string, but with all five or more letter words reversed (Just like the
# name of this Kata). Strings passed in will consist of only letters and
# spaces. Spaces will be included only when more than one word is present.
# Examples:
# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# spinWords( "This is a test") => returns "This is a test"
# spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(sentence):
    list_of_words = sentence.split()

    for word in list_of_words:
        if len(word) >= 5:
            list_of_words.insert(list_of_words.index(word), word[::-1])
            list_of_words.remove(word)

    return " ".join(list_of_words)


# ____________________________________________________________________________
# Task 6 (6 kyu)
# Your task is to sort a given string. Each word in the string will contain a
# single number. This number is the position the word should have in the
# result.Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# If the input string is empty, return an empty string. The words in the input
# String will only contain valid consecutive numbers.
# Examples:
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"

def order(sentence):
    list_for_dct_keys = []
    list_for_new_string = []

    [list_for_dct_keys.append(int(element)) for element in sentence if
     element.isdigit()]

    dct = dict(zip(list_for_dct_keys, sentence.split()))

    counter = 1
    for key, value in dct.items():
        word = dct.get(counter)
        list_for_new_string.append(word)
        counter += 1

    return " ".join(list_for_new_string)
