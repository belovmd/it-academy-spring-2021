"""Homework 3 - Task 5"""


def print_unique_elements(lst: list) -> None:
    """Уникальные элементы в списке

    Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
    Элементы нужно выводить в том порядке, в котором они встречаются в списке.
    """
    elements_counts = {}
    for element in lst:
        elements_counts[element] = elements_counts.get(element, 0) + 1
    for key in elements_counts:
        if elements_counts[key] == 1:
            print(key, end=' ')


if __name__ == '__main__':
    print_unique_elements([1, 2, 3, 2, 4, 3, 5, 'ab', 'bc', 'ab'])
