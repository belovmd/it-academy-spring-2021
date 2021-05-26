"""
Homework 5 - Task4
В файле хранятся данные с сайта IMDB. Скопированные данные
хранятся в файле ./data_hw5/ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
"""


dct_imdb250 = {}
dct_years = {}
dct_ratings = {}


def write_result(dct_, file_, hist=0):
    with open(file_, 'w') as fh1:
        for k, v in dct_.items():
            if hist:
                fh1.write(str(k) + ": " + "*" * v + "\n")
            else:
                fh1.write(str(k) + ": " + v + "\n")
        fh1.close()


try:
    with open('data_hw5/ratings.list', 'r') as fh:
        lst_imdb250 = fh.readlines()[28:278]
        fh.close()

except FileNotFoundError:
    print('Error: File not found!')

else:
    for line_index in range(len(lst_imdb250)):
        dist, votes, rank, *title, year = lst_imdb250[line_index].split()
        dct_imdb250.setdefault(line_index + 1, ' '.join([str(word) for word in title]))

        if int(year[1:5]) in dct_years:
            dct_years[int(year[1:5])] += 1
        else:
            dct_years.setdefault(int(year[1:5]), 1)

        if float(rank) in dct_ratings:
            dct_ratings[float(rank)] += 1
        else:
            dct_ratings.setdefault(float(rank), 1)

    write_result(dct_imdb250, 'top250_movies.txt')
    write_result(dct_ratings, 'ratings.txt', hist=1)
    write_result(dct_years, 'years.txt', hist=1)
