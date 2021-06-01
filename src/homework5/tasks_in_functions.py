def delete_of_punctuation():
    sentence = str(input())
    punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]
    for symbol in punctuation:
        sentence = sentence.replace(symbol, ' ')
    print(sentence)


def the_longest_word():
    sentence = str(input())
    words = sentence.split(' ')
    longest_word = ''

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    print('Самое длинное слово', longest_word)
