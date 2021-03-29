"""Homework2 - task4"""

some_string = "Explicit is better, than Implicit."
counter_big_letters = 0
counter_small_letters = 0

for char in some_string:
    if 'a' <= char <= 'z':
        counter_small_letters += 1
    elif 'A' <= char <= 'Z':
        counter_big_letters += 1

print(counter_small_letters)
print(counter_big_letters)
