s = 'Hello WorlD'
k = len(s)
b = 0
n = 0
for i in range(k):
    if 65 <= ord(s[i]) <= 90:
        b += 1
    if 97 <= ord(s[i]) <= 122:
        n += 1

print('Прописные', b)
print('Строчные', n)
