import string


def all_sum_hw2_1():
    # Напишите программу, которая считает общую цену.
    # Вводится M рублей и N копеек цена, а также количество S товара
    # Посчитайте общую цену в рублях и копейках за L товаров.

    M = int(input('Введите стоимость (рублей) : '))
    N = int(input('Введите стоимость (копеек) : '))
    S = int(input('Введите количество товара (шт.) : '))
    L = int(input('Введите количество покупаемого товара (шт.) : '))

    price_one_item = (M * 100 + N) / S
    m_l = int(price_one_item * L) // 100
    n_l = int(price_one_item * L) % 100

    print('Общая цена {} рублей {} копеек'.format(m_l, n_l))


def longest_word_hw2_2():
    # Самое длинное слово.
    # Найти самое длинное слово в введенном предложении.
    # Учтите что в предложении есть знаки препинания.

    my_str = "Днём позже, днём раньше - какая разница."
    my_str = "".join(ch_ for ch_ in my_str if ch_ not in string.punctuation)

    words = my_str.split(' ')

    long = 0
    longest_word = words[0]

    for word in words:
        if len(word) > long:
            long = len(word)
            longest_word = word

    print('Самое длинное слово :', longest_word)


def clear_string_hw2_3():
    # Вводится строка.
    # Требуется удалить из нее повторяющиеся символы и все пробелы.
    # Например, если было введено "abc cde def", то должно быть выведено "abcdef".

    my_str = input('Введите строку: ')
    new_str = ''

    for i in my_str:
        if i not in new_str and i != ' ':
            new_str += i

    print(new_str)


def upper_and_lower_hw2_4():
    # Строчные и прописные
    # Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
    # Учитывать только английские буквы.

    my_str = input('Введите строку : ')

    lowercase_counter = len([ch_ for ch_ in my_str if 'a' <= ch_ <= 'z'])
    uppercase_counter = len([ch_ for ch_ in my_str if 'A' <= ch_ <= 'Z'])

    print('Строчных : {}. Прописных : {}'.format(lowercase_counter, uppercase_counter))


def fib_hw2_5():
    # Число Фибоначчи.
    # Выведите n-ое число Фибоначчи, используя только временные переменные,
    # циклические операторы и условные операторы.

    n = int(input('Введите n : '))

    if n == 1 or n == 2:
        print('Ответ : ', 1)
    else:
        f1 = 1
        f2 = 1
        i = 2
        while i < n:
            f1, f2 = f2, f1 + f2
            i = i + 1
        print('Ответ : ', f2)


def palindrome_hw2_6():
    # Палиндром.
    # Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
    # Число положительное целое, произвольной длины.
    # Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще)

    num = int(input('Введите число : '))

    if num < 10:
        print('Однозначное число!!!')
    else:
        n = num
        rev_n = 0
        while n > 0:
            units = n % 10
            rev_n = rev_n * 10 + units
            n = n // 10

        if num == rev_n:
            print('Палиндром')
        else:
            print('Не палиндром')


def triangle_hw2_7():
    # Треугольник.
    # Даны: три стороны треугольника.
    # Требуется: проверить, действительно ли это стороны треугольника.
    # Если стороны определяют треугольник, найти его площадь.
    # Если нет, вывести сообщение о неверных данных.

    side_a = float(input('Введите длину первой стороны треугольнка : '))
    side_b = float(input('Введите длину второй стороны треугольнка : '))
    side_c = float(input('Введите длину третьей стороны треугольнка : '))

    if side_a >= side_b + side_c or side_b >= side_a + side_c or side_c >= side_a + side_b:
        print('Неверные данные!')
    else:
        perimeter = (side_a + side_b + side_c) / 2
        square = (perimeter * (perimeter - side_a) *
                  (perimeter - side_b) * (perimeter - side_c)) ** 0.5
        print('Площадь данного треугольника : ', square)


def fizzbuzz_hw3_1():
    # FizzBuzz
    # Напишите программу, которая печатает цифры от 1 до 100,
    # но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5
    # пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz

    for num in range(1, 101):
        if not num % 3 and not num % 5:
            print('FizzBuzz')
        elif not num % 3:
            print('Fizz')
        elif not num % 5:
            print('Buzz')
        else:
            print(num)


def list_practice_hw3_2():
    # List practice
    # 1. Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
    # 2. Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
    # 3. Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
    # 4. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
    # 5. Скопируйте список и добавьте в него элемент '2a' так
    # чтобы в исходном списке этого элемента не было.

    list_for_task1 = [chr1 + chr2 for chr1 in ['a', 'b'] for chr2 in ['b', 'c', 'd']]
    list_for_task2 = list_for_task1[::2]
    list_for_task3 = [str(chr_) + 'a' for chr_ in range(1, 5)]
    print(list_for_task3.pop(1))  # task4
    list_for_task5 = list_for_task3[:] + ['2a']


def tuple_practice_hw3_3():
    # Tuple practice
    # 1. Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
    # 2. Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
    # 3. Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
    # 4. Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы
    # последовательно выводились значения 1, 2, 3.
    # Убедитесь что len() исходного кортежа возвращает 1.

    tuple_for_task1 = tuple(['a', 'b', 'c'])
    list_for_task2 = list(('a', 'b', 'c'))
    a, b, c = ('a', 2, 'python')  # task3
    tuple_for_task4 = ([1, 2, 3],)

    print(len(tuple_for_task4))


def couple_hw3_4():
    # Пары элементов
    # Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
    # Считается, что любые два элемента, равные друг другу образуют одну пару,
    # которую необходимо посчитать.
    # Входные данные - строка из чисел, разделенная пробелами.
    # Выходные данные - количество пар.
    # Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар

    input_str = input()
    lst = input_str.split()
    counter = 0

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                counter += 1

    print(counter)


def unique_hw3_5():
    # Уникальные элементы в списке
    # Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
    # Элементы нужно выводить в том порядке, в котором они встречаются в списке.

    lst = [1, 2, 3, 4, 3, 2, 7]
    print(*[element for element in lst if lst.count(element) == 1])


def sort_list_hw3_6():
    # Упорядоченный список
    # Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка,
    # не меняя их порядок, а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя,
    # дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку.
    # Распечатайте полученный список.

    lst = [1, 3, 0, 5, 0, 0, 7, 0, 3]
    index = len(lst) - 1
    while index > 0:
        if not lst[index]:
            lst.append(lst.pop(index))
        index -= 1

    print(lst)


def dict_comprehensions_hw4_1():
    # Dict comprehensions
    # Создайте словарь с помощью генератора словарей,
    # так чтобы его ключами были числа от 1 до 20,
    # а значениями кубы этих чисел.

    result = {index: index ** 3 for index in range(1, 21)}
    print(result)


def cities_hw4_2():
    # Города
    # Дан список стран и городов каждой страны.
    # Затем даны названия городов.
    # Для каждого города укажите, в какой стране он находится.
    # Входные данные
    # Программа получает на вход количество стран N.
    # Далее идет N строк, каждая строка начинается с названия страны,
    # затем идут названия городов этой страны.
    # В следующей строке записано число M,
    # далее идут M запросов — названия каких-то M городов,
    # перечисленных выше.
    # Выходные данные
    # Для каждого из запроса выведите название страны,
    # в котором находится данный город.

    num_of_countries = int(input())
    data = {}
    while num_of_countries > 0:
        line = input().split()
        data[line[0]] = line[1:]
        num_of_countries -= 1

    requests = []
    num_of_requests = int(input())
    while num_of_requests:
        requests.append(input())
        num_of_requests -= 1

    for request in requests:
        for country in data.keys():
            if request in data[country]:
                print(country)


def lists1_hw4_3():
    # Даны два списка чисел.
    # Посчитайте, сколько различных чисел содержится
    # одновременно как в первом списке, так и во втором

    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]

    print(len((set(list1)) & set(list2)))


def lists2_hw4_4():
    # Даны два списка чисел.
    # Посчитайте, сколько различных чисел
    # входит только в один из этих списков

    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]

    print(len((set(list1)) ^ set(list2)))


def languages_hw4_5():
    # Языки
    # Каждый из N школьников некоторой школы знает Mi языков.
    # Определите, какие языки знают все школьники и языки,
    # которые знает хотя бы один из школьников.

    num_of_schoolboys = int(input())
    schoolboy_lang = {}
    all_lang = set()

    while num_of_schoolboys:
        num_of_lang = int(input())
        schoolboy_lang[num_of_schoolboys] = set()
        while num_of_lang:
            lang_ = input()
            all_lang.add(lang_)
            schoolboy_lang[num_of_schoolboys].add(lang_)
            num_of_lang -= 1
        num_of_schoolboys -= 1

    general_lang = all_lang.copy()
    for lang in schoolboy_lang.values():
        general_lang &= lang

    un_lang = all_lang.copy()
    for lang in schoolboy_lang.values():
        un_lang |= lang

    print(len(general_lang), *general_lang, sep='\n')
    print(len(un_lang), *un_lang, sep='\n')


def words_hw4_6():
    # Слова
    # Во входной строке записан текст.
    # Словом считается последовательность непробельных символов идущих подряд,
    # слова разделены одним или большим числом пробелов или символами конца строки.
    # Определите, сколько различных слов содержится в этом тексте.

    input_str = "qwerty qwerty qwerty       qwerty max"
    print(len(set(input_str.split())))


def numbers_hw4_7():
    # Даны два натуральных числа.
    # Вычислите их наибольший общий делитель
    # при помощи алгоритма Евклида
    # (мы не знаем функции и рекурсию).

    a = int(input())
    b = int(input())

    while a and b:
        if a > b:
            a %= b
        else:
            b %= a

    print(max(a, b))
