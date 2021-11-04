# В файле хранятся данные с сайта IMDB. Скопированные данные
# хранятся в файле ./data_hw5/ ratings.list.
# Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
# Найдите ТОП250 фильмов и извлеките заголовки.
# Программа создает 3 файла  top250_movies.txt – названия файлов,
# ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.

import os.path

if os.path.exists('ratings.list'):
    with open('ratings.list', 'r') as fh:
        years = {}
        ranks = {}
        films = ''
        marker = False
        for str_ in fh:
            if str_.strip() == 'New  Distribution  Votes  Rank  Title':
                marker = True
            elif str_.strip() == 'BOTTOM 10 MOVIES (1500+ VOTES)':
                break
            elif marker and str_.strip() != '':
                str_words = str_.split()
                str_words = str_words[2: len(str_words)]
                year = str_words[-1].strip('()/I')
                years[year] = years.get(year, 0) + 1
                rank = str_words[0]
                ranks[rank] = ranks.get(rank, 0) + 1
                film = ' '.join(str_words[1:-1])
                films += film + '\n'

    histogram_years = ''
    histogram_ranks = ''

    for key, value in years.items():
        histogram_years += '{}: {}\n'.format(key, value)
    for key, value in ranks.items():
        histogram_ranks += '{}: {}\n'.format(key, value)
    with open('top250_movies.txt', 'w') as fh:
        fh.write(films)
    with open('ratings.txt', 'w') as fh:
        fh.write(histogram_ranks)
    with open('years.txt', 'w') as fh:
        fh.write(histogram_years)

else:
    print('404')
