"""В файле хранятся данные с сайта IMDB.

Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
"""
import matplotlib.pyplot as plt
import pandas as pd
import re
import seaborn as sns


def gist_build(data_lst, file_name):
    data_lst.sort()
    data_set = set(data_lst)
    with open(file_name, 'w') as fh:
        for element in data_set:
            fh.writelines('| {} {}\n'.format(element, '+' * data_lst.count(element)))


file_lst = []
lst_index = []
count = 0

try:
    with open('./data_hw5/ratings.list') as fh:
        for line in fh.readlines():
            if line.startswith('New'):
                count += 1
                lst_index.append(count)
                file_lst.append(line.strip().split('  '))
            else:
                count += 1
                file_lst.append(line.strip().split('  '))
except IOError:
    print("File not found!")

top_250 = [file_lst[lst_index[0] + row] for row in range(250)]  # список топ 250 фильмов

# создаем список с названиеми фильмов и записываем их в файл
titles = [top_250[num][-1].split() for num in range(len(top_250))]
titles = [' '.join(titles[num][:-1]) for num in range(len(titles))]
with open('top250_movies.txt', 'w') as fh:
    for title in titles:
        fh.writelines('{}\n'.format(title))

# создаем отсортированный список рейтингов и записываем в файл гистограмму
ratings = [float(top_250[num][2]) for num in range(len(top_250) - 1)]
gist_build(ratings, 'ratings.txt')

# создаем отсортированный список по годам и записываем в файл гистограмму
years = [int(re.findall(r'[(](\d{4})', str(top_250[num]))[0]) for num in range(len(top_250))]
gist_build(years, 'years.txt')

# создадим таблицу с помощью pandas
columns = file_lst[lst_index[0] - 1]  # шапка таблицы
data = pd.DataFrame(top_250, index=range(1, 251), columns=columns[1:])

# рисуем гистограмму в matplotlib и seaborn
plt.style.use('classic')  # задаем стили
sns.set()

# создадим гистограмму рейтингов
fig_rank = plt.figure()  # создаем область для рисования
plt.hist(data['Rank'].sort_values(), alpha=0.5)  # рисуем гистограмму рейтингов
plt.title('Распределение лучших фильмов по рейтингу')
plt.xlabel('Рейтинг')
plt.ylabel('Количество, шт.')
fig_rank.savefig('ranks.png')  # сохраняем в файл в формете png

# создадим гистограмму годов
fig_y = plt.figure()
ax_y = plt.axes()
plt.xlim(1900, 2040)
years_pd = pd.Series(years)
plt.hist(x=years_pd, alpha=0.5)
plt.title('Распределение лучших фильмов по годам')
plt.xlabel('Год')
plt.ylabel('Количество, шт.')
fig_y.savefig('years.png')
