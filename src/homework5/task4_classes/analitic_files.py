import matplotlib.pyplot as plt
import copy


class AnalyzeFilms:

    def __init__(self, dict_):
        self.__analyze_films = copy.deepcopy(dict_)
        self.rank_list = self.__get_rank_list("Rank")
        self.years_list = self.__get_years_list("Years")

    def __get_rank_list(self, key):
        lst_ = list()
        for elem in self.__analyze_films.values():
            lst_.append(float(elem[key]))
        return lst_

    def __get_years_list(self, key):
        lst_ = list()
        for elem in self.__analyze_films.values():
            lst_.append(int(elem[key]))
        return lst_

    def plot_hist_rank(self):
        bins = list(set(self.rank_list)).sort()
        plt.hist(self.rank_list, bins=bins, edgecolor="black")
        plt.title("Movie rating")
        plt.ylabel("Count of films")
        plt.xlabel("Rank")
        plt.savefig('./task4_output_files/ratings.png')

    def plot_hist_years(self):
        bins = list(set(self.years_list)).sort()
        plt.hist(self.years_list, bins=bins, edgecolor="black")
        plt.title("Release films")
        plt.ylabel("Count of films")
        plt.xlabel("Years")
        plt.savefig('./task4_output_files/years.png')





