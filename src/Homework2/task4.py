# Task 4. Посчитать количество строчных (маленьких) и прописных (больших) букв
# в введенной строке. Учитывать только английские буквы.

my_string = "Lorem ipsUm dolor Sit amet, CoNseCtetur ADIpiscing " \
            "ELIT".replace(' ', '').replace(',', '')

lowercase = [letter for letter in my_string if letter.islower()]

print("Uppercase letters:", (len(my_string) - len(lowercase)),
      "\nlowercase letters:", len(lowercase))
