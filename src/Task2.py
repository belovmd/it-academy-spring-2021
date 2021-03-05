def find_longest_word(sentence):
    longest_word = ''
    for word in sentence.split():
        word_to_check = word.strip('!,.:;,-')
        if len(word_to_check) > len(longest_word):
            longest_word = word_to_check
    return longest_word


# TEST
print(find_longest_word('Найти, самое длинное слово в введенном предложении!'))
