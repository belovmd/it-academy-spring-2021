list_numbers = [int(number) for number in input().split()]
len_list = len(list_numbers)
print('Количество пар: ', int((len_list * (len_list - 1)) / 2))
