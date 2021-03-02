# task №17: "8-Queens Problem(recursion)"
BOARD_SIZE = 8


def under_attack(col, queens_number):
    left = right = col

    for r, c in reversed(queens_number):
        left, right = left - 1, right + 1

        if c in (left, col, right):
            return True
    return False


def solve(n):
    if n == 0:
        return [[]]

    smaller_solutions = solve(n - 1)

    return [solution + [(n, queen + 1)]
            for queen in range(BOARD_SIZE)
            for solution in smaller_solutions
            if not under_attack(queen + 1, solution)]


for answer in solve(BOARD_SIZE):
    print(answer)
