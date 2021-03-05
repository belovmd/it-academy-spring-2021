string = input("Введите предложение, а мы покажем вам какое из слов \nв вашем предложении самое длинное.")

for i in string:
    if i == ',' or i == '.':
        string = string.replace(i, "")

my_list = string.split()
long = ''

for j in my_list:
    if len(j) > len(long):
        long = j

print(long)
