string = input("Введите строку, а мы удалим из нее все пробелы и повторяющиеся символы.")

for i in string:
    if i == ' ':
        string = string.replace(i, '')

newstring = string[0]
for j in string[1:]:
    if j not in newstring:
        newstring += j

print(newstring)
