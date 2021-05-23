# Data processing from the IMDB website.
import os.path


if os.path.exists('ratings.list'):
    with open('ratings.list', 'r') as fh:
        n = 0
        dict_years = {}
        dict_rat = {}
        films = ""
        for line in fh:
            if 27 < n < 278:
                words = line.split()
                words = words[2:len(words)]
                rate = words.pop(0)
                year = (words.pop(len(words) - 1)).strip("(,)")
                dict_rat[rate] = dict_rat.get(rate, 0) + 1
                dict_years[year] = dict_years.get(year, 0) + 1
                films += " ".join(words) + "\n"
            elif n > 278:
                break
            n += 1
    histogram_rat = ""
    histogram_years = ""
    for key, value in dict_rat.items():
        histogram_rat += "{}:{}\n".format(key, value)
    for key, value in dict_years.items():
        histogram_years += "{}:{}\n".format(key, value)
    with open('top250_movies.txt', 'w') as fh:
        fh.write(films)
    with open('ratings.txt', 'w') as fh:
        fh.write(histogram_rat)
    with open('years.txt', 'w') as fh:
        fh.write(histogram_years)
else:
    print("file does not exist")
