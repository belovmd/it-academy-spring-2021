my_string = [i for i in input().split()]
new_string = []
length = 0
longest_word = ''
for word in my_string:
    new_string.append(word.strip(",.?!:;"))
for word in new_string:
    if len(word) > length:
        length = len(word)
        longest_word = word
print(longest_word)
