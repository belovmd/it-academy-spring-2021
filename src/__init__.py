import re

# 1
print('Hello world!')

# 2
name = input('What is your name?\n')
print('Hi, %s.' % name) # %s это спецификатор подстановки строки

# 3
friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):  # Функция создаёт объект, генерирующий кортежи,
    # состоящие из индекса элемента и самого этого элемента.
    print("iteration {iteration} is {name}".format(iteration=i, name=name))

# 4
parents, babies = (1, 1)
while babies < 100:
    print ('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)


# 5
def greet(name):
    print('Hello', name)


greet('Jack')
greet('Jill')
greet('Bob')


# 6

for test_string in ['555-1212', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print(test_string, 'is a valid US local phone number')
    else:
        print(test_string, 'rejected')


# 7
prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print('I owe the grocer $%.2f' % grocery_bill)
