"""Homework 3 - Task 6"""


def print_sorted_list(lst: list) -> None:
    """Упорядоченный список.

    Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка,
    не меняя их порядок, а все нули - в правую часть.
    Порядок ненулевых элементов изменять нельзя, дополнительный список использовать нельзя,
    задачу нужно выполнить за один проход по списку.
    Распечатайте полученный список.
    """
    index, zeros_count = 0, 0
    while index < len(lst) - zeros_count:
        if not lst[index]:
            lst.append(lst.pop(index))
            zeros_count += 1
            continue
        index += 1
    print(*lst, end=' ')


if __name__ == '__main__':
    print_sorted_list([0, 1, 0, 2, 3, 4, 0])
