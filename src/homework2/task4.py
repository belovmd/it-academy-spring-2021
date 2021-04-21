# 4. Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы.


text = '''Lorem Ipsum industry's'''
print("Entered text: ", text)

print('Total number of elements in entered text = ', len(text))

space_marks = 0
for i in text :
  if i == " " or i == "," or i == "." or i == "/" or i == "(" or i == ")" or i == "[" or i == "]" or i == "{" or i == "}" or i == ";" or i == ":":
    space_marks += 1

text = text.replace(',', '')
text = text.replace('.', '')
text = text.replace('/', '')
text = text.replace('//', '')
text = text.replace('(', '')
text = text.replace(')', '')
text = text.replace('[', '')
text = text.replace(']', '')
text = text.replace('{', '')
text = text.replace('}', '')
text = text.replace(';', '')
text = text.replace('...', '')
text = text.replace(':', '')
text = text.replace(' ', '')

small_letters = 0
big_letters = 0
other_symbols = 0

for i in text:
  if i >= 'a' and i <= 'z':
    small_letters += 1
  else:
      if i >= 'A' and i <= 'Z':
        big_letters += 1
      else:
        if i == "'":
          other_symbols += 1

print('Number of small letters in entered text = ', small_letters)
print('Number of big letters in entered text = ', big_letters)
print('Number of other symbols in words of entered text = ', other_symbols)
print('Number of spaces and punctuation marks in entered text = ', space_marks)


#  elif i == ",":
#    space_marks += 1
#  elif i == ".":
#    space_marks += 1
#  elif i == "/":
#    space_marks += 1
#  elif i == "(":
#    space_marks += 1
#  elif i == ")":
#    space_marks += 1
#  elif i == "[":
#    space_marks += 1
#  elif i == "]":
#    space_marks += 1
#  elif i == "{":
#    space_marks += 1
#  elif i == "}":
#    space_marks += 1
#  elif i == ";":
#    space_marks += 1
#  elif i == "^":
#    space_marks += 1