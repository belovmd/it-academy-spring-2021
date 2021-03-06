import re


text = "Good апар morning апрапр Mr АБ рпап Jhonson апрпа"
new_string = re.sub(r'[а-яёА-ЯЁ]', "", text)
upper_chars = 0
lower_chars = 0
for char in new_string:
    if char.isalpha():
        if char.isupper():
            upper_chars += 1
        elif char.islower():
            lower_chars += 1
print("Cтрочные буквы: {} \nПрописные буквы: {} \n".format(lower_chars, upper_chars))
