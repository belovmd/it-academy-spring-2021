def calculate_letters(text):
    uppercase_alphabet = ("ABCDEFGHIJKLMNO"
                          "PQRSTUVWXYZ")
    lower_case_alphabet = uppercase_alphabet.lower()
    upper = 0
    lower = 0
    for element in text:
        if element in uppercase_alphabet:
            upper += 1
        elif element in lower_case_alphabet:
            lower += 1
    template = "in string {} cursive letters and {} lowercase letters"
    print(template.format(upper, lower))


sentence = ("Walking, running, cycling and "
            "playing football are some kinds "
            "of sports that you do every day.")
calculate_letters(sentence)
