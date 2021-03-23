# Условие:
# Not all of the elements are important. What you need to do
# here is to remove from the list all of the elements before the given one.
# For the illustration we have a list [1, 2, 3, 4, 5] and we need to remove
# all elements that go before 3 - which is 1 and 2.
# We have two edge cases here: (1) if a cutting element cannot be found, then
# the list shouldn't be changed. (2) if the list is empty, then it should remain empty.
# Input: List and the border element.
# Output: Iterable (tuple, list, iterator ...).
# Ссылка:
# https://py.checkio.org/mission/remove-all-before/solve/

# noinspection PyGlobalUndefined
def remove_all_before(items: list, border: int):
    global number
    finish_list = []
    if border not in items:
        return items
    else:
        for number in items:
            if number == border:
                break
        for num in range(items.index(number), len(items)):
            finish_list.append(items[num])
        return finish_list


print(remove_all_before([1, 2, 3, 4, 5], 3))
