import random

random.seed(100500)

lst1 = [random.randint(0, 10) for elem in range(20)]
lst2 = [random.randint(0, 10) for elem in range(20)]
count_diff_elem = len(set(lst1) ^ set(lst2))
print(count_diff_elem)
