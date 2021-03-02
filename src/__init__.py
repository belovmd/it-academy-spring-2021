import re

print('Hello world!')

name = input('What is your name?\n')
print('Hi, %s.' % name)  # %s это спецификатор подстановки строки

friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):  # Функция создаёт объект, генерирующий кортежи,
    # состоящие из индекса элемента и самого этого элемента.
    print("iteration {iteration} is {name}".format(iteration=i, name=name))

parents, babies = (1, 1)
while babies < 100:
    print('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)


def greet(func_name):
    print('Hello', func_name)


greet('Jack')
greet('Jill')
greet('Bob')

for test_string in ['555-1212', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print(test_string, 'is a valid US local phone number')
    else:
        print(test_string, 'rejected')

prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print('I owe the grocer $%.2f' % grocery_bill)
