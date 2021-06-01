"""
IMDB

В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла:
top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов,
years.txt – гистограмма годов.
"""


def dict_top250():
    """Функция возвращает словарь типа:

    {Порядковый_№_фильма: [Название, год, рейтинг]}
    """

    dict_top_250 = dict()
    index = 1
    topX = 250
    len_distribution = 10
    try:
        with open('ratings.list', 'r') as rating_list:

            while len(dict_top_250) != topX:
                line = rating_list.readline()
                formatted_line = line.strip().split()
                if formatted_line and \
                        formatted_line[0].isdigit() and \
                        len(formatted_line[0]) == len_distribution:
                    dict_top_250[index] = [' '.join(formatted_line[3:-1]),
                                           int(formatted_line[-1][1:5]),
                                           float(formatted_line[2])]
                    index += 1
        return dict_top_250
    except FileNotFoundError:
        print('File Not Found')


def create_top_250():
    """Функция создает и наполняет

    списком фильмов файл top250_movies.txt
    """

    with open('top250_movies.txt', 'w') as file_:
        index = 1
        for film in (dict_top250().values()):
            file_.writelines('{}. {}\n'.format(index, film[0]))
            index += 1


def create_bar_graph_rating():
    """Функция создает гистограмму

    рейтинга фильмов и записывает ее
    в файл ratings.txt
    """

    dict_ = {}
    for film_ in dict_top250().values():
        if film_[2] in dict_.keys():
            dict_[film_[2]] += 1
        else:
            dict_[film_[2]] = 1

    with open('ratings.txt', 'w') as file_:
        for element in sorted(dict_.keys()):
            line = '{} : {}\n'.format(element, '*' * dict_[element])
            file_.writelines(line)


def create_bar_graph_years():
    """Функция создает гистограмму

    годов выпуска фильмов и записывает ее
    в файл years.txt
    """

    dict_ = {}
    for film_ in dict_top250().values():
        if film_[1] in dict_.keys():
            dict_[film_[1]] += 1
        else:
            dict_[film_[1]] = 1

    with open('years.txt', 'w') as file_:
        for element in sorted(dict_.keys()):
            line = '{} : {}\n'.format(element, '*' * dict_[element])
            file_.writelines(line)


create_top_250()
create_bar_graph_rating()
create_bar_graph_years()
