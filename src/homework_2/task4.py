my_string = input('Посчитать количество строчных (маленьких) и прописных (больших)\n'
                  'букв в введенной строке. Учитывать только английские буквы.')

print('Большие', sum(map(str.isupper, my_string)), 'маленькие', sum(map(str.islower, my_string)))
