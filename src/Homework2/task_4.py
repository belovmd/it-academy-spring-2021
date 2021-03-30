# Task 4. Посчитать количество строчных (маленьких) и прописных (больших) букв
# в введенной строке. Учитывать только английские буквы.

my_string = "Lorem ipsUm dolor Sit amet, CoNseCtetur ADIpiscing " \
            "ELIT".replace(' ', '')

lowercase = [letter for letter in my_string if letter == letter.lower()]

print("Uppercase letters:", (len(my_string) - len(lowercase)),
      "\nlowercase letters:", len(lowercase))
