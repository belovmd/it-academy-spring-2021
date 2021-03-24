input_string = "abc cde def def abc"
new_string = ""

for char in input_string:
    if char != " ":
        if char not in new_string:
            new_string = new_string + char
print(new_string)
