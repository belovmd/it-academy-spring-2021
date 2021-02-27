print('Hello, world!')
name = input('What is your name?\n')
parents, babies = (1, 1)
while babies < 100:
    print('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)


def greet(firstname):
    print('Hello', firstname)


greet('Jack')
greet('Jill')
greet('Bob')
