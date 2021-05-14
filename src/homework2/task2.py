# 2. Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
# Подсказки:
# my_string.split([chars]) возвращает список строк.
# len(list) - количество элементов в списке

# ------------------------------------------------------------------------------------ #

sent = input()
# sent = '''Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
# when an unknown printer took a galley of type and scrambled it to make a type specimen book.'''
# text = sent.copy()
print(len(sent))
sent = sent.replace(',', '')
sent = sent.replace('.', '')
sent = sent.replace('/', '')
sent = sent.replace('//', '')
sent = sent.replace('(', '')
sent = sent.replace(')', '')
sent = sent.replace('[', '')
sent = sent.replace(']', '')
sent = sent.replace('{', '')
sent = sent.replace('}', '')
sent = sent.replace(';', '')
sent = sent.replace('...', '')
sent = sent.replace(':', '')
text = sent.split(' ')
print(text)
print(max(text, key=len))
