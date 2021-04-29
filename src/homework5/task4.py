"""В файле хранятся данные с сайта IMDB.

Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# создадим вспомогательные списки для поиска нужных данных
file_lst = []   # список состоящий из строк файла
lst_index = []  # список номеров строк с которых начинаются таблицы с данными
count = 0       # счетчик для нумерации строк

try:
    with open('ratings.list') as fh:  # откроем файл, если такой существует
        for line in fh.readlines():
            if line.startswith('New'):  # поиск строки с заголовками таблицы
                count += 1
                lst_index.append(count)  # добавляем номер необходимой строки
                file_lst.append(line.strip().split('  '))
            else:
                count += 1
                file_lst.append(line.strip().split('  '))
except IOError:  # выводим дружественное сообщение, если файл не найден
    print("File not found!")

top_250 = file_lst[lst_index[0]:lst_index[0] + 250]  # список тор 250 фильмов

# создаем список с названиеми фильмов и записываем их в файл
titles = [str(top_250[num][-1])[:-7] for num in range(len(top_250))]
with open('top250_movies.txt', 'w') as fh:
    for title in titles:
        fh.writelines('{}\n'.format(title))

# создаем отсортированный список рейтингов и записываем в файл гистограмму
ratings = [float(top_250[num][2]) for num in range(len(top_250) - 1)]
ratings.sort()
ratings_set = set(ratings)
with open('ratings.txt', 'w') as fh:
    for rating in ratings_set:
        fh.writelines('| {} {}\n'.format(rating, '+' * ratings.count(rating)))

# создаем отсортированный список по годам и записываем в файл гистограмму
years_cell = [str(top_250[num][-1]).strip().split(' (')
              for num in range(len(top_250))]
years = [int(years_cell[num][1][:4]) for num in range(len(years_cell) - 1)]
years.sort()
years_set = set(years)
with open('years.txt', 'w') as fh:
    for year in years_set:
        fh.writelines('| {} {}\n'.format(year, '+' * years.count(year)))

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
