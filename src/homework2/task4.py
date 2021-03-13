# Посчитать количество строчных (маленьких) и прописных (больших) букв
# в введенной строке. Учитывать только английские буквы.
str_ = "PROCESS finished"
lower_letter = 0
upper_letter = 0
for letter in str_:
    if "a" <= letter <= "z":
        lower_letter += 1
    elif "A" <= letter <= "Z":
        upper_letter += 1
print(lower_letter)
print(upper_letter)
