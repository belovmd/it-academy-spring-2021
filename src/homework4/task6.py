"""Слова

Во входной строке записан текст.
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте.
"""


def count_words(str_):
    return len(str_.split())


# test
print(count_words("adksldj2e32   9219 9210ds\nfhjs''sdsad \b\n adsdasd \n \tjijhk"))
