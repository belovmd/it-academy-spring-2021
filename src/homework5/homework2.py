def homework2_task1():
    def count_total_amount(ruble, kopeck, quantity_of_goods):
        if ruble < 0 or kopeck < 0 or quantity_of_goods < 0:
            return "Перепроверьте данные"
        total_rub_amount = ruble * quantity_of_goods
        total_kop_amount = kopeck * quantity_of_goods
        while total_kop_amount > 100:
            total_rub_amount += 1
            total_kop_amount -= 100
        return f"Общая цена {total_rub_amount} рублей {total_kop_amount} копеек"

    print(count_total_amount(3, 20, 3))
    print(count_total_amount(-3, 20, 3))


def homework2_task2():
    def find_longest_word(sentence):
        longest_word = ''
        for word in sentence.split():
            word_to_check = word.strip('!,.:;,-')
            if len(word_to_check) > len(longest_word):
                longest_word = word_to_check
        return longest_word

    print(find_longest_word('Найти, самое длинное слово в введенном предложении!'))


def homework2_task3():
    def remove_repetition(sentence):
        resulting_str = ''
        str_to_check = sentence.replace(' ', '')
        while len(str_to_check):
            resulting_str += str_to_check[0]
            str_to_check = str_to_check.replace(str_to_check[0], '')
        return resulting_str

    print(remove_repetition("abc cde def"))


def homework2_task4():
    def count_upper_and_lower(string):
        upper = 0
        lower = 0
        for letter in string:
            ascii_num = ord(letter)
            if ascii_num > 64 and ascii_num < 91:
                upper += 1
                print(letter)
            elif ascii_num > 96 and ascii_num < 123:
                lower += 1
        return f"String contain {upper} capital and {lower} lowercase letters"

    print(count_upper_and_lower('CounT    LoweR    ANd UPper LetTerS!      '))


def homework2_task5():
    def find_n_fibonacci(num):
        if num <= 1:
            return 1
        previous = 0
        actual = 1
        for i in range(1, num):
            temp = actual
            actual += previous
            previous = temp
        return actual

    print(find_n_fibonacci(8))


def homework2_task6():
    def is_palindrome(num):
        value_to_divide = num
        value_to_check = 0

        while value_to_divide > 0:
            value_to_check = value_to_check * 10 + (value_to_divide % 10)
            value_to_divide //= 10

        return value_to_check == num
        print(is_palindrome(12321))


def homework2_task7():
    def is_triangle(a, b, c):
        if (a + b > c) and (a + c > b) and (b + c > a):
            p = (a + b + c) / 2
            s_squared = p * (p - a) + (p - b) * (p - c)
            s = s_squared ** 0.5
            print(f"Площадь треугольника равна {s}")
        else:
            print("Перепроверьте данные")

    is_triangle(5, 7, 9)
