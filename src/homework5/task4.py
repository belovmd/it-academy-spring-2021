# Task 4 — В файле хранятся данные с сайта IMDB. Скопированные данные хранятся
# в файле /data_hw5/ ratings.list. Откройте и прочитайте файл(если его нет
# необходимо вывести ошибку). Найдите ТОП250 фильмов и извлеките заголовки.
# Программа создает 3 файла  top250_movies.txt – названия файлов, ratings.txt
# – гистограмма рейтингов, years.txt – гистограмма годов.


def headers(lst):
    for line in lst:
        if line == "New  Distribution  Votes  Rank  Title":
            return lst.index(line) + 1


def cleaning_lines(lst):
    working_list = []
    for line in lst:
        working_line = line.replace("   ", "  ").split("  ")
        for item in working_line:
            item.strip()
            if not item:
                working_line.remove(item)
        working_list.append(working_line)
    return working_list


def info_for_docs(lst):
    film, year, rating = [], [], []
    for line in lst:
        movie = line[-1].replace("(", "").replace(")", "")
        year.append(movie.split()[-1])
        film.append(" ".join(movie.split()[:-1]))
        rating.append(line[2])
    return film, year, rating


def cleaning_dates(lst):
    for item in lst:
        if item.endswith("/I"):
            clean_item = item[:4]
            lst[lst.index(item)] = clean_item
    return lst


def writing_in_files(file, lst):
    file_for_writing = open(file, "w")
    for item in lst:
        file_for_writing.write(item)
        file_for_writing.write("\n")
    file_for_writing.close()
    return


def histogram(lst):
    dict_, histogram_list = {}, []
    for item in lst:
        if item in dict_.keys():
            dict_[item] += 1
        else:
            dict_[item] = 1
    for keys in sorted(dict_.keys(), reverse=True):
        histogram_list.append("{}: {}".format(keys, "*" * dict_[keys]))
    return histogram_list


text = []
with open("ratings.list", "r") as original:
    for i in original.readlines():
        text.append(i.strip())

list_of_250_strings = text[headers(text):headers(text)+250]
list_of_movies = cleaning_lines(list_of_250_strings)
films, years, ratings = info_for_docs(list_of_movies)
years = cleaning_dates(years)

writing_in_files("top250_movies.txt", films)
writing_in_files("ratings.txt", histogram(ratings))
writing_in_files("years.txt", histogram(years))
