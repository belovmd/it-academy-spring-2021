import copy


class TextReader:

    def __init__(self, path):
        self.__inf_about_movies = dict()
        try:
            self.__file = open(r"{}".format(path), encoding='utf-8', errors='ignore')
        except FileNotFoundError:
            print("Файл не существует")

    def __del__(self):
        try:
            self.__file.close()
        except AttributeError:
            print("Не может закрыть не существующий файл")

    def __move_ref_string(self, pattern):
        while pattern not in self.__file.readline():
            pass

    def __add_to_cache(self, line):
        inf_movie = [elem for elem in (line.strip()).split()]
        film_name = " ".join(inf_movie[3:len(inf_movie) - 1])
        years = inf_movie[-1][1:5]
        rank = inf_movie[2]
        self.__inf_about_movies[film_name] = {"Years": years, "Rank": rank}

    def find_top_250_movies(self):
        self.__move_ref_string("New  Distribution  Votes  Rank  Title")
        count = 250
        while count:
            str_ = self.__file.readline()
            self.__add_to_cache(str_)
            count -= 1

    def show_dict(self):
        for key, value in self.__inf_about_movies.items():
            print("Name {} | Value {}".format(key, value))

    def get_films_dict(self):
        return copy.deepcopy(self.__inf_about_movies)

    def close_file(self):
        self.__file.close()

    def write_top_films_to_file(self):
        file_top_250 = open("./task4_output_files/top250_movies.txt ", 'w')
        for key in self.__inf_about_movies.keys():
            file_top_250.write(key + "\n")
        file_top_250.close()
