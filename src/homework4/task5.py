def enter_data():
    print("Входные данные")
    count_student = int(input())
    dict_stud_lang = {}
    while count_student:
        count_languages = int(input())
        set_ = set()
        while count_languages:
            language = input()
            set_.add(language)
            count_languages -= 1
        dict_stud_lang[count_student] = set_
        count_student -= 1
    print(dict_stud_lang)


enter_data()