"""
В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла:
top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов,
years.txt – гистограмма годов.
"""

import os.path


if os.path.exists('./data_hw5/ratings.list'):
    with open('./data_hw5/ratings.list', 'r') as fh:
        n = 0
        dict_years = {}
        dict_rating = {}
        films = ""
        start = False
        for line in fh:
            if line.strip() == "New  Distribution  Votes  Rank  Title":
                start = True
            elif line.strip() == "BOTTOM 10 MOVIES (1500+ VOTES)":
                break
            elif start and line.strip() != "":
                words = line.split()
                words = words[2:len(words)]
                rate = words.pop(0)
                year = (words.pop(len(words) - 1)).strip("(,)")
                dict_rating[rate] = dict_rating.get(rate, 0) + 1
                dict_years[year] = dict_years.get(year, 0) + 1
                films += " ".join(words) + "\n"

    histogram_rat = ""
    histogram_years = ""
    for key, value in dict_rating.items():
        histogram_rat += "{}:{}\n".format(key, value)
    for key, value in dict_years.items():
        histogram_years += "{}:{}\n".format(key, value)
    with open('top250_movies.txt', 'w') as fh:
        fh.write(films)
    with open('ratings.txt', 'w') as fh:
        fh.write(histogram_rat)
    with open('years.txt', 'w') as fh:
        fh.write(histogram_years)
else:
    print("file does not exist")
