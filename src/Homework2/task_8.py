# TASK 8. TASKS FROM CODEWARS

# Task 1 (7 kyu):
# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

def get_count(input_str):
    num_vowels = 0

    for element in input_str:
        if element in ['a', 'o', 'e', 'i', 'u']:
            num_vowels += 1

    return num_vowels


# ____________________________________________________________________________
# Task 2: (7 kyu)
# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

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
# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

def disemvowel(original_str):
    vowels = ['a', 'o', 'u', 'e', 'i']

    for letter in original_str:
        if letter in vowels or letter.lower() in vowels:
            original_str = original_str.replace(letter, "")

    return original_str


# ____________________________________________________________________________
# Task 4 (6 kyu)
# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

def find_it(sequence):

    for number in sequence:
        if sequence.count(number) % 2 != 0:
            break

    return number


# ____________________________________________________________________________
# Task 5 (6 kyu)
# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

def spin_words(sentence):
    list_of_words = sentence.split()

    for word in list_of_words:
        if len(word) >= 5:
            list_of_words.insert(list_of_words.index(word), word[::-1])
            list_of_words.remove(word)

    return " ".join(list_of_words)


# ____________________________________________________________________________
# Task 6 (6 kyu)
# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

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
