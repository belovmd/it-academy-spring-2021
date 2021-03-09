# Найти самое длинное слово в введенном предложении.
txt = input()
maxlen = 0
maxword = []

for word in txt.split():
    L = len(word)
    if L > maxlen:
        maxlen = L
        maxword = [word]
    elif L == maxlen:
        maxword.append(word)
print('самое длинное слово', maxword, 'состоит из', maxlen, 'букв')
