string = input()
finish_string = []
for element in string:
    if element not in finish_string:
        finish_string.append(element)
finish_string.remove(' ')
finish_string = ''.join(finish_string)
print(finish_string)
