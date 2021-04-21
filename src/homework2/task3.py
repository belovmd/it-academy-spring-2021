# 3. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".


#3. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы. Например, если было введено "abc cde def", то должно быть выведено "abcdef".
text = '''abc cde def'''
print(text)
text = text.replace(',', '')
text = text.replace('.', '')
text = text.replace('/', '')
text = text.replace('//', '')
text = text.replace('(', '')
text = text.replace(')', '')
text = text.replace('[', '')
text = text.replace(']', '')
text = text.replace('{', '')
text = text.replace('}', '')
text = text.replace(';', '')
text = text.replace('...', '')
text = text.replace(':', '')
text = text.replace(' ', '')
final_text = sorted(set(text))
print(final_text)
print(''.join(final_text))