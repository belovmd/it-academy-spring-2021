def presses(phrase):
    """Multi-tap Keypad Text Entry on an Old Mobile Phone

    Prior to having fancy iPhones,
    teenagers would wear out their thumbs sending SMS messages
    on candybar-shaped feature phones with 3x4 numeric keypads.

    ------- ------- -------
    |     | | ABC | | DEF |
    |  1  | |  2  | |  3  |
    ------- ------- -------
    ------- ------- -------
    | GHI | | JKL | | MNO |
    |  4  | |  5  | |  6  |
    ------- ------- -------
    ------- ------- -------
    |PQRS | | TUV | | WXYZ|
    |  7  | |  8  | |  9  |
    ------- ------- -------
    ------- ------- -------
    |     | |space| |     |
    |  *  | |  0  | |  #  |
    ------- ------- -------
    Prior to the development of T9 (predictive text entry) systems,
    the method to type words was called "multi-tap" and
    involved pressing a button repeatedly
    to cycle through the possible values.

    For example, to type a letter "R" you would press the 7 key three times
    (as the screen display for the current character cycles through P->Q->R->S->7).
    A character is "locked in" once the user presses a different key or pauses
    for a short period of time (thus, no extra button presses
    are required beyond what is needed for each letter individually).
    The zero key handles spaces,
    with one press of the key producing a space and two presses producing a zero.

    In order to send the message "WHERE DO U WANT 2 MEET L8R"
    a teen would have to actually do 47 button presses.
    No wonder they abbreviated.

    For this assignment, write a module that can calculate the amount of button
    presses required for any phrase. Punctuation can be ignored for this exercise.
    Likewise, you can assume the phone doesn't distinguish between upper/lowercase characters
    (but you should allow your module to accept input in either for convenience).

    Hint: While it wouldn't take too long to hard code the amount of keypresses
    for all 26 letters by hand, try to avoid doing so!
    (Imagine you work at a phone manufacturer who might be
    testing out different keyboard layouts, and you want to be able to test new ones rapidly.)
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
    stack = []
    for element in string:
        if element == '(':
            stack.append(')')
        if element == ')':
            if not stack:
                return False
            else:
                stack.pop()

    return not stack


def sum_pairs(ints, s):
    """Sum of Pairs

    Given a list of integers and a single sum value,
    return the first two values
    (parse from the left please) in order of
    appearance that add up to form the sum.
    """
    set_of_int = set(ints)  # множесто из входных чисел
    valid_pairs = []  # пары чисел удовлетворяющие условию
    result = {}  # словарь-результат : {длина промежутка : [пара_пара_чисел]}
    for iterator_1 in set_of_int:
        for iterator_2 in set_of_int:
            if iterator_1 + iterator_2 == s:
                if not valid_pairs.count([iterator_1, iterator_2]):
                    valid_pairs.append([iterator_1, iterator_2])

    if valid_pairs:
        for a, b in valid_pairs:
            index_a = ints.index(a)
            index_b = ints.index(b)
            if a != b:
                if index_a != index_b:
                    if index_a < index_b:
                        result[index_b - index_a] = [a, b]
                    else:
                        result[index_a - index_b] = [b, a]
            elif a == b and ints.count(a) > 1:
                result[ints[index_a + 1:].index(a) - index_a] = [a, a]

    if result:
        return result[min(result.keys())]  # вывод результата с наименьшим промежутком
    else:
        return None


def format_duration(seconds):
    """Human readable duration format

    Your task in order to complete this Kata
    is to write a function which formats a duration,
    given as a number of seconds, in a human-friendly way.

    The function must accept a non-negative integer.
    If it is zero, it just returns "now".
    Otherwise, the duration is expressed as a combination of
    years, days, hours, minutes and seconds.

    It is much easier to understand with an example:

    format_duration(62)    # returns "1 minute and 2 seconds"
    format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
    For the purpose of this Kata, a year is 365 days and a day is 24 hours.

    Note that spaces are important.

    Detailed rules
    The resulting expression is made of components like 4 seconds, 1 year, etc.
    In general, a positive integer and one of the valid units of time,
    separated by a space. The unit of time is used in plural if the integer is greater than 1.

    The components are separated by a comma and a space (", ").
    Except the last component, which is separated by " and ",
    just like it would be written in English.

    A more significant units of time will occur before than a least significant one.
    Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

    Different components have different unit of times.
    So there is not repeated units like in 5 seconds and 1 second.

    A component will not appear at all if its value happens to be zero.
    Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

    A unit of time must be used "as much as possible".
    It means that the function should not return 61 seconds,
    but 1 minute and 1 second instead.
    Formally, the duration specified by of a component
    must not be greater than any valid more significant unit of time.
    """
    if not seconds:
        return 'now'

    year = (seconds // 31536000)
    day = (seconds - year * 31536000) // 86400
    hour = (seconds - year * 31536000 - day * 86400) // 3600
    minute = (seconds - year * 31536000 - day * 86400 - hour * 3600) // 60
    second = (seconds - year * 31536000 - day * 86400 - hour * 3600 - minute * 60) % 60

    result_list = []

    if year:
        result_list.append('{} year{}'.format(year, 's' if year > 1 else ''))
    if day:
        result_list.append('{} day{}'.format(day, 's' if day > 1 else ''))
    if hour:
        result_list.append('{} hour{}'.format(hour, 's' if hour > 1 else ''))
    if minute:
        result_list.append('{} minute{}'.format(minute, 's' if minute > 1 else ''))
    if second:
        result_list.append('{} second{}'.format(second, 's' if second > 1 else ''))

    if len(result_list) == 1:
        return result_list[0]
    elif len(result_list) == 2:
        return '{} and {}'.format(result_list[0], result_list[1])
    elif len(result_list) == 3:
        return '{}, {} and {}'.format(result_list[0], result_list[1],
                                      result_list[2])
    elif len(result_list) == 4:
        return '{}, {}, {} and {}'.format(result_list[0], result_list[1],
                                          result_list[2], result_list[3])
    elif len(result_list) == 5:
        return '{}, {}, {}, {} and {}'.format(result_list[0], result_list[1],
                                              result_list[2], result_list[3],
                                              result_list[4])
