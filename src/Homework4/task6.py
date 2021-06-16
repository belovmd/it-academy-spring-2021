"""
Task6.

Во входной строке записан текст.
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов
или символами конца строки.
Определите, сколько различных слов содержится в этом тексте.
"""

str_1 = """
Во входной строке записан текст.\n
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов\n или символами конца строки.
Определите, сколько различных слов\n содержится в этом тексте.
"""

str_2 = "asd \n d   d"


def count_unique_words(input_str):
    input_str = input_str.replace('\n', ' ')
    s = set(input_str.split(' '))
    s.discard('')
    return len(s)


print(count_unique_words(str_1))
print(count_unique_words(str_2))


def count_unique_words_v2(input_str):
    return len(set(input_str.split()))


print(count_unique_words_v2(str_1))
print(count_unique_words_v2(str_2))
