# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
str_ = "abc cde def"
str_new = ""
for i in str_:
    if i not in str_new and i != " ":
        str_new += i
print(str_new)
