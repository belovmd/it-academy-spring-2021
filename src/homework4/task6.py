# task6

# Во входной строке записан текст. Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.

str_ = input().split()
print(len(set(str_)), 'Различных слов в данном тексте')
