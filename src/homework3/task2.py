import copy

list_1 = [letter1 + letter2 for letter1 in 'ab' for letter2 in 'bcd']
list_1 = list_1[::2]

list_2 = [symbol1 + symbol2 for symbol1 in '1234' for symbol2 in 'a']
print(list_2.pop(1))
list_2new = copy.deepcopy(list_2)
list_2new.append('2a')
print(list_1, list_2, list_2new, sep='\n')
