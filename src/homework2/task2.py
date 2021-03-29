"""Homework2 - task2"""

import string

input_string = "Explicit is better, than implicit."

input_string = "".join(char for char in input_string if char not in string.punctuation)
word_list = input_string.split()
word_max_len = (len(max(word_list, key=len)))

for current_word in word_list:
    if len(current_word) == word_max_len:
        print(current_word)
