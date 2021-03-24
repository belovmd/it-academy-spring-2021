"""
Create a function that will return a string that combines
all of the letters of the three inputed strings in groups.

Taking the first letter of all of the inputs and grouping
them next to each other. Do this for every letter, see
example below!

E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"

Note: You can expect all of the inputs to be the same length.
"""

first_string = "LLh"
second_string = "euo"
third_string = "xtr"
last_string = ""
result_string = first_string + second_string + third_string

for char in range(len(first_string)):
    slicer = result_string[char::len(first_string)]
    last_string += slicer

print(last_string)
