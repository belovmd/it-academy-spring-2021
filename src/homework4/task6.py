import re

str_ = "Hello  tom     How are \n you How \n Are yor feelling \n\n\n glad"
count = len(re.split(r"\s+", str_))
print(count)  # Если нужно, переделаю не через регулярные выражения.
