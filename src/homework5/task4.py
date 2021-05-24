"""Homework 5 - Task 4

В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле  ./data_hw5/ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла:
  - top250_movies.txt – названия файлов,
  - ratings.txt – гистограмма рейтингов,
  - years.txt – гистограмма годов.
"""


def imdb_data(source_file):

    def split_line(keys, line, delimiter):
        """
        Функция возвращает словарь, позиционно сопоставляя список ключей keys (имен сторлбцов
        таблицы) со списком значений, полученных в результате разбиения строки таблицы данных line
        в список подстрок по разделителю delimiter.

        Проблема в том, что в экземпляре исходного файла каждая строка данных начинается с
        6 пробелов. Основываясь на описании формата, а именно "New movies are indicated
        by a "*" before their entry", и * отсутствует в начале строки данных, предполагаем, что 6
        пробелов - это разделитель столбцов New и Distribution и поэтому для правильного разбиения
        заменяем их на delimiter.
        """

        lst = line.replace(' ' * 6, delimiter, 1).split(delimiter)
        data = dict(zip(keys, lst))
        # выделение года, помещенного в скобки в конце названия каждого фильма, из названия и
        # помещение в отдельный ключ словаря
        data['Year'] = data['Title'][-4:-1]
        # удаление года из названия фильма
        data['Title'] = data['Title'][:-7]
        return data

    try:
        with open(source_file) as reader, open('top250_movies.txt', 'w') as writer:

            line, title_row = '?', 'New  Distribution  Votes  Rank  Title\n'
            # поиск первой строки заголовка, за которой следуют строки данных топ250 фильмов
            while line and line != title_row:
                line = reader.readline()
            if not line:
                return None

            keys = title_row.rstrip().split(' ' * 2)
            # keys.append('Year')  # добавление года к списку столбцов
            ranks = {}
            years = {}
            counter = 0
            while True:
                line = reader.readline().rstrip()
                if not line:  # прерывание цикла чтения, при достижении незаполненной строки
                    break

                row = split_line(keys, line, delimiter=' ' * 2)

                counter += 1
                # вывод в файл списка названий фильмов с номером по порядку
                writer.write('{counter} {title}\n'.format(
                    counter=str(counter).rjust(3),
                    title=row['Title']
                ))

                # подсчет количество фильмов с одинаковым рейтингом
                ranks[row['Rank']] = ranks.get(row['Rank'], 0) + 1
                # подсчет количество фильмов, выпущенных в один год
                years[row['Year']] = years.get(row['Year'], 0) + 1

    except FileNotFoundError:
        print('Error: source file "{file_name}" is not exist.'.format(file_name=source_file))

    # вывод в файл гистограммы рейтингов фильмов
    with open('ratings.txt', 'w') as writer:
        for rank, movies_count in ranks.items():
            writer.write('Rank {rank} | {gist} {movies_count}\n'.format(
                rank=rank,
                gist='*' * movies_count,
                movies_count=str(movies_count) + ' movies' if movies_count > 1 else 'movie'
            ))

    # вывод в файл гистограммы годов выхода фильмов в прокат
    with open('years.txt', 'w') as writer:
        years = sorted(years.items(), key=lambda item: str(item[-1]) + item[0], reverse=True)
        for year, movies_count in years:
            writer.write('Year {year} | {gist} {movies_count}\n'.format(
                year=year,
                gist='*' * movies_count,
                movies_count=str(movies_count) + (' movies' if movies_count > 1 else ' movie')
            ))


if __name__ == '__main__':

    imdb_data('D:/ratings.list')
