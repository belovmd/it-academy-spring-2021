#  6. Слова
#  Во входной строке записан текст.
#  Словом считается последовательность непробельных символов идущих подряд,
#  слова разделены одним или большим числом пробелов или символами конца
#  строки.
#  Определите, сколько различных слов содержится в этом тексте.

# ------------------------------------------------------------------------------------ #

line = '''
Lorem\r Ipsum has    been\n the industry's    standard dummy\n
text ever since the\t 1500s, when an unknown printer took a \n
        galley      of type and     scrambled it to make a type
specimen \tbook.'''

print("Entered text: ", line)
line_2 = line.strip().split()
print("1:", line_2)
clear_data = []
#  punctuation_marks = '''.,:;...!?&\n\t\r\\ '''
line_2 = [i.replace('.', '').replace(',', '').replace(':', '').replace(';', '').replace('!', '').replace('!', '')
          .replace('?', '').replace('#', '').replace('&', '') for i in line_2]
print("2:", line_2)
line_3 = list(set(line_2))
print("3:", line_3)
print("Total amount of different words in line:", len(line_3))
