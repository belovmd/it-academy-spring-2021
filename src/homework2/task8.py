"""Homework2 - task8

Зарегистрируйтесь на одном (или нескольких) из сайтов:
https://py.checkio.org/ , https://www.codewars.com,   https://www.hackerrank.com/, https://acmp.ru
И решите 1-5 задач уровня Elementary и advanced.
Поместите 3 простых и 2 сложных задачи на Ваш выбор в пул реквест.

"""


def alphabet_position(text):
    """Replace With Alphabet Position (6 kyu):

    https://www.codewars.com/kata/546f922b54af40e1e90001da/python
    In this kata you are required to, given a string, replace every letter with its position in the
    alphabet. If anything in the text isn't a letter, ignore it and don't return it.
    "a" = 1, "b" = 2, etc.
    Example:
        alphabet_position("The sunset sets at twelve o' clock.")
        should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
        (as a string)
    """

    return ' '.join(
        str(ord(c) - ord('a') + 1) for c in text.lower() if ord('a') <= ord(c) <= ord('z'))


def unique_in_order(iterable):
    """Unique In Order (6 kyu): https://www.codewars.com/kata/54e6533c92449cc251001667

    Implement the function unique_in_order which takes as argument a sequence and returns a list of
    items without any elements with the same value next to each other and preserving the original
    order of elements.
    Example:
        unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
        unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
        unique_in_order([1,2,2,3,3])       == [1,2,3]
    """

    return [c for i, c in enumerate(iterable) if not i or iterable[i - 1] != c]


def dir_reduction(arr):
    """Directions Reduction (5 kyu): https://www.codewars.com/kata/550f22f4d758534c1100025a

    Write a function dir_reduction which will take an array of strings and returns an array of
    strings with the needless directions removed (W<->E or S<->N side by side).
    Example:
        dir_reduction(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]) == ["WEST"]
        dir_reduction(["NORTH", "WEST", "SOUTH", "EAST"]) == ["NORTH", "WEST", "SOUTH", "EAST"]
    """

    class Stack:

        def __init__(self):
            self.__stack = []

        def __bool__(self):
            return bool(self.__stack)

        def push(self, element):
            self.__stack.append(element)

        def peek(self):
            if self.__bool__():
                return self.__stack[-1]
            else:
                raise IndexError('peek from empty stack')

        def pop(self):
            if self.__bool__():
                peek_val = self.peek()
                self.__stack.pop()
                return peek_val
            else:
                raise IndexError('pop from empty stack')

        def list_of_elements(self):
            return self.__stack[:]

    stack = Stack()
    removed_directions = ({'NORTH', 'SOUTH'}, {'EAST', 'WEST'})
    for direction in arr:
        if not stack or not {direction, stack.peek()} in removed_directions:
            stack.push(direction)
        else:
            stack.pop()
    return stack.list_of_elements()


def snail(matrix):
    """Snail (4 kyu): https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

    Given an n x n array, return the array elements arranged from outermost elements to the middle
    element, traveling clockwise.
    Example:
        array = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]
        snail(array) => [1,2,3,6,9,8,7,4,5]
    """

    size = len(matrix)
    turns = size // 2 + size % 2
    res = []

    for turn in range(turns):
        corrector = size % 2 * (turn + 1) // turns  # 1 for the last turn on odd sizes, else 0
        res.extend(matrix[turn][turn: size - turn])
        res.extend([matrix[i][size - 1 - turn] for i in range(turn + 1, size - 1 - turn)])
        res.extend(reversed(matrix[size - 1 - turn][turn + corrector: size - turn]))
        res.extend(reversed([matrix[i][turn] for i in range(turn + 1, size - 1 - turn)]))

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

    print('-------------- dir_reduction tests ----------------')
    test = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    assert dir_reduction(test) == ['WEST'], 'Failed - test1'
    test = ["NORTH", "WEST", "SOUTH", "EAST"]
    assert dir_reduction(test) == ["NORTH", "WEST", "SOUTH", "EAST"], 'Failed - test2'
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
