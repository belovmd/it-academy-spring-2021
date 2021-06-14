# В файле хранятся данные с сайта IMDB.
# Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
# Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
# Найдите ТОП250 фильмов и извлеките заголовки.
# Программа создает 3 файла:
#  1. top250_movies.txt – названия файлов
#  2. ratings.txt – гистограмма рейтингов
#  3. years.txt – гистограмма годов


import os.path


if os.path.exists('ratings.list'):
    with open('ratings.list', 'r') as fh:
        years_histogram = {}
        ratings_histogram = {}
        films = []
        for linenum, line in enumerate(fh):
            if 27 < linenum < 278:
                line = line.split()
                films.append(' '.join(line[3:-1]))
                rating = line[2]
                ratings_histogram[rating] = ratings_histogram.get(rating, 0) + 1
                year = line[-1]
                years_histogram[year] = years_histogram.get(year, 0) + 1
            elif linenum > 278:
                break

    with open('top250_movies.txt', 'w') as fh:
        for film in films:
            fh.write(film + '\n')

    with open('years.txt', 'w') as fh:
        for year in years_histogram:
            fh.write(f'{year.strip("()")}:{years_histogram[year]}' + '\n')

    with open('ratings.txt', 'w') as fh:
        for rating in ratings_histogram:
            fh.write(f'{rating}:{str(ratings_histogram[rating])}' + '\n')
else:
    print('error, no such file exists')
