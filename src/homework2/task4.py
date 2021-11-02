# 4. Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы.

# ------------------------------------------------------------------------------------ #

text2 = '''Lorem Ipsum industry's'''
print("Entered text: ", text2)

marks = ',.///()[]{};...:'
for mark in marks:
    text2.replace(mark, '')

space_marks2 = 0
for i in text2:
    if i == marks or i == ' ':
        space_marks2 += 1

small_letters2 = 0
big_letters2 = 0
other_symbols2 = 0

for i in text2:
    if 'a' <= i <= 'z':  # if i >= 'a' and i <= 'z':
        small_letters2 += 1
    elif 'A' <= i <= 'Z':  # elif i >= 'A' and i <= 'Z':
        big_letters2 += 1
    elif i == "'":
        other_symbols2 += 1

print('Total number of elements in entered text = ', len(text2))
print('Number of small letters in entered text = ', small_letters2)
print('Number of big letters in entered text = ', big_letters2)
print('Number of other symbols in words of entered text = ', other_symbols2)
print('Number of spaces and punctuation marks in entered text = ', space_marks2)
