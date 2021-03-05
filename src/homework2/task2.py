import re

text = "2. Найти самое длинное слово в введенном предложении. Учтите что в " \
      "предложении есть знаки препинания. "
string_list = re.split(r"[ ,:;.-]+", text)
max_length = len(string_list[0])
result_string = None
for current_string in string_list:
    if max_length < len(current_string):
        max_length = len(current_string)
        result_string = current_string
print(result_string)
