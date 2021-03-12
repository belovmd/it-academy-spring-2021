"""Homework2 - task8

Зарегистрируйтесь на одном (или нескольких) из сайтов:
https://py.checkio.org/ , https://www.codewars.com,   https://www.hackerrank.com/, https://acmp.ru
И решите 1-5 задач уровня Elementary и advanced.
Поместите 3 простых и 2 сложных задачи на Ваш выбор в пул реквест.

"""


def alphabet_position(text):
    """Replace With Alphabet Position (6 kyu)
    https://www.codewars.com/kata/546f922b54af40e1e90001da/python

    In this kata you are required to, given a string, replace every letter with its position in the
    alphabet. If anything in the text isn't a letter, ignore it and don't return it.
    "a" = 1, "b" = 2, etc.
    Example:
        alphabet_position("The sunset sets at twelve o' clock.")
        should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
        (as a string)
    """

    return ' '.join(str(ord(c) - ord('a') + 1) for c in text.lower() if ord('a') <= ord(c) <= ord('z'))


def unique_in_order(iterable):
    """Unique In Order (6 kyu)
    https://www.codewars.com/kata/54e6533c92449cc251001667

    Implement the function unique_in_order which takes as argument a sequence and returns a list of
    items without any elements with the same value next to each other and preserving the original
    order of elements.
    Example:
        unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
        unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
        unique_in_order([1,2,2,3,3])       == [1,2,3]
    """

    return [c for i, c in enumerate(iterable) if not i or iterable[i - 1] != c]


def dir_reduc(arr):
    """Directions Reduction (5 kyu)
    https://www.codewars.com/kata/550f22f4d758534c1100025a

    Write a function dir_reduc which will take an array of strings and returns an array of strings
    with the needless directions removed (W<->E or S<->N side by side).
    Example:
        dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]) == ["WEST"]
        dir_reduc(["NORTH", "WEST", "SOUTH", "EAST"]) == ["NORTH", "WEST", "SOUTH", "EAST"]
    """

    stack = []
    for direction in arr:
        if not stack or not {direction, stack[-1]} in ({'NORTH', 'SOUTH'}, {'EAST', 'WEST'}):
            stack.append(direction)
        else:
            stack.pop()
    return stack


def snail(matrix):
    """Snail (4 kyu)
    https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

    Given an n x n array, return the array elements arranged from outermost elements to the middle
    element, traveling clockwise.
    Example:
        array = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]
        snail(array) #=> [1,2,3,6,9,8,7,4,5]
    """

    size = len(matrix)
    turns = size // 2 + size % 2
    res = []
    for turn in range(turns):
        excluder = size % 2 * (turn + 1) // turns
        res.extend(matrix[turn][turn: size - turn])
        res.extend([matrix[i][size - 1 - turn] for i in range(turn + 1, size - 1 - turn)])
        res.extend(matrix[size - 1 - turn][-turn - 1: -size - 1 + excluder + turn: -1])
        res.extend([matrix[i][turn] for i in range(size - 2 - turn, turn, -1)])
    return res


if __name__ == '__main__':
    print('------------ alphabet_position tests --------------')
    test = "The sunset sets at twelve o' clock."
    assert alphabet_position(test) == ('20 8 5 19 21 14 19 5 20 19 5 20 19 ' 
                                       '1 20 20 23 5 12 22 5 15 3 12 15 3 11'), 'Failed - test1'
    print('Done!')

    print('------------- unique_in_order tests ---------------')
    test = 'AAAABBBCCDAABBB'
    assert unique_in_order(test) == ['A', 'B', 'C', 'D', 'A', 'B'], 'Failed - test1'
    test = 'ABBCcAD'
    assert unique_in_order(test) == ['A', 'B', 'C', 'c', 'A', 'D'], 'Failed - test2'
    test = [1, 2, 2, 3, 3]
    assert unique_in_order(test) == [1, 2, 3], 'Failed - test3'
    print('Done!')

    print('---------------- dir_reduc tests ------------------')
    test = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    assert dir_reduc(test) == ['WEST'], 'Failed - test1'
    test = ["NORTH", "WEST", "SOUTH", "EAST"]
    assert dir_reduc(test) == ["NORTH", "WEST", "SOUTH", "EAST"], 'Failed - test2'
    print('Done!')

    print('------------------ snail tests --------------------')
    test = [[1]]
    assert snail(test) == [1], 'Failed - test1'
    test = [[1, 2],
            [3, 4]]
    assert snail(test) == [1, 2, 4, 3], 'Failed - test2'
    test = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    assert snail(test) == [1, 2, 3, 6, 9, 8, 7, 4, 5], 'Failed - test3'
    test = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]
    assert snail(test) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10], 'Failed - test4'
    print('Done!')
