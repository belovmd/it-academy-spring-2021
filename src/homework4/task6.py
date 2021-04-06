"""Homework 4 - Task 6"""


def different_words_number(input_text: str) -> int:
    """Слова

    Во входной строке записан текст. Словом считается последовательность непробельных символов
    идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.
    Определите, сколько различных слов содержится в этом тексте.
    """
    return len({word for word in input_text.split() if word})


if __name__ == '__main__':

    text = """aaaaa bbb   ccccc
        ddd aaaaa eee bbb fffff
        eee"""

    print(different_words_number(text))
