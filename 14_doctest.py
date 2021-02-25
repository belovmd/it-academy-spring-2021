# task №14: "Doctest-based testing"
import doctest


def median(pool):
<<<<<<< HEAD

    # Statistical median to demonstrate doctest.
    # >>> median([2, 9, 9, 7, 9, 2, 4, 5, 8])
    # 6 change to 7 in order to pass the test"""
=======
"""Statistical median to demonstrate doctest.
>>> median([2, 9, 9, 7, 9, 2, 4, 5, 8])
6 #change to 7 in order to pass the test
"""
>>>>>>> 9bca17d6d3beb019fcd9193d194755838a852f9e

    copy = sorted(pool)
    size = len(copy)
    if size % 2 == 1:
        return copy[int((size - 1) / 2)]
    else:
        return (copy[int(size / 2 - 1)] + copy[int(size / 2)]) / 2


if __name__ == '__main__':
    doctest.testmod()
