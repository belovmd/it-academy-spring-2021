# task №11: "Triple-quoted strings, while loop"
REFRAIN = '''
%d bottles of beer on the wall,
%d bottles of bear,
take one down, pass it around,
%d battles of beer on the wall!
'''
bottles_of_beer = 9
while bottles_of_beer > 1:
    print(REFRAIN % (bottles_of_beer, bottles_of_beer, bottles_of_beer - 1))
    bottles_of_beer -= 1
