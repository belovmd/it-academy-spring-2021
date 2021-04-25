'''
В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
'''


from task4_classes.analitic_files import AnalyzeFilms
from task4_classes.find_information import TextReader


films = TextReader(
    "./data_hw5/ratings.list")
films.find_top_250_movies()
films.write_top_films_to_file()
analyze = AnalyzeFilms(
    films.get_films_dict())
analyze.plot_hist_years()      # Одну гистограмму сдела в txt файле
analyze.plot_hist_rank()       # Другую с помощью matplotlib. Файлы поместил в папку task4_output_files
