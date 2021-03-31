def presses(phrase):
    """Multi-tap Keypad Text Entry on an Old Mobile Phone

    Prior to having fancy iPhones,
    teenagers would wear out their thumbs sending SMS messages on
    candybar-shaped feature phones with 3x4 numeric keypads.
    """

    keyboard = {'1', 'ABC2', 'DEF3', 'GHI4', 'JKL5',
                'MNO6', 'PQRS7', 'TUV8', 'WXYZ9', ' 0', '#', '*'}
    count = 0
    for k in phrase.upper():
        for el in keyboard:
            if k in el:
                count += el.index(k) + 1

    return count


def move_zeros(array):
    """Moving Zeros To The End

    Write an algorithm that takes an array and
    moves all of the zeros to the end,
    preserving the order of the other elements.
    """
    return [x for x in array if x] + [x for x in array if not x]


def make_readable(seconds):
    """Human Readable Time

    Write a function, which takes a non-negative integer (seconds)
    as input and returns the time in a human-readable format (HH:MM:SS)
    """
    hh = seconds // 3600
    mm = (seconds - hh * 3600) // 60
    ss = seconds - hh * 3600 - mm * 60

    return '{}:{}:{}'.format(hh if hh // 10 else ('0' + str(hh)),
                             mm if mm // 10 else ('0' + str(mm)),
                             ss if ss // 10 else ('0' + str(ss)))


def alphabet_position(text):
    """Replace With Alphabet Position

    In this kata you are required to,
    given a string,
    replace every letter with its position in the alphabet.
    """
    alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
                'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16,
                'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                'x': 24, 'y': 25, 'z': 26}

    result = ''

    for ch_ in text.lower():
        if ch_ in alphabet:
            result += str(alphabet[ch_]) + ' '

    return result[:-1]


def valid_parentheses(string):
    """Valid Parentheses

    Write a function that takes a string of parentheses,
    and determines if the order of the parentheses is valid.
    The function should return true if the string is valid,
    and false if it's invalid.
    """
    count = 0

    for x in string:
        if x == '(':
            count += 1
        elif x == ')':
            if not count:
                return False
            count -= 1

    if not count:
        return True
    else:
        return False
