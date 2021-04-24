"""Homework 5 - Task 4

В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data_hw5/ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла:
  - top250_movies.txt – названия файлов,
  - ratings.txt – гистограмма рейтингов,
  - years.txt – гистограмма годов.
"""


def imdb_data(source_file):

    try:
        with open(source_file) as reader, open('top250_movies.txt', 'w') as writer:

            line, title_row = '?', 'New  Distribution  Votes  Rank  Title\n'
            while line and line != title_row:
                line = reader.readline()
            if not line:
                return None

            keys = title_row.rstrip().split(' ' * 2)
            keys.append('Year')
            # title_border = 30
            ranks = {}
            years = {}
            counter = 0
            while True:
                line = reader.readline().rstrip()
                if not line:
                    break
                line = line.replace(' ' * 4, '-', 1).replace(' (', '  (')
                row = dict(zip(keys, line.split(' ' * 2)))
                # row['Rank'] = float(row['Rank'])
                row['Year'] = row['Year'][1:5]

                counter += 1
                writer.write('{counter} {title}\n'.format(
                    counter=str(counter).rjust(3),
                    title=row['Title']
                ))

                ranks[row['Rank']] = ranks.get(row['Rank'], 0) + 1
                years[row['Year']] = years.get(row['Year'], 0) + 1

    except FileNotFoundError:
        print('Error: source file "{file_name}" is not exist.'.format(file_name=source_file))

    with open('ratings.txt', 'w') as writer:
        for rank, movies_count in ranks.items():
            writer.write('Rank {rank} | {gist} {movies_count}\n'.format(
                rank=rank,
                gist='*' * movies_count,
                movies_count=str(movies_count) + ' movies' if movies_count > 1 else 'movie'
            ))

    with open('years.txt', 'w') as writer:
        years = sorted(years.items(), key=lambda item: str(item[-1]) + item[0], reverse=True)
        for year, movies_count in years:
            writer.write('Year {year} | {gist} {movies_count}\n'.format(
                year=year,
                gist='*' * movies_count,
                movies_count=str(movies_count) + (' movies' if movies_count > 1 else ' movie')
            ))


if __name__ == '__main__':

    imdb_data('ratings.list')

# --------------------------------------------------------------------------------------------------
# top250_movies.txt
# --------------------------------------------------------------------------------------------------
#   1 The Shawshank Redemption
#   2 The Godfather
#   3 The Godfather: Part II
#   4 The Dark Knight
#   5 12 Angry Men
#   6 Schindler's List
#   7 Pulp Fiction
#   8 The Lord of the Rings: The Return of the King
#   9 Il buono, il brutto, il cattivo
#  10 Fight Club
#  11 The Lord of the Rings: The Fellowship of the Ring
#  12 Forrest Gump
#  13 Star Wars: Episode V - The Empire Strikes Back
#  14 Inception
#  15 The Lord of the Rings: The Two Towers
#  16 One Flew Over the Cuckoo's Nest
#  17 Goodfellas
#  18 The Matrix
#  19 Shichinin no samurai
#  20 Star Wars
#  21 Cidade de Deus
#  22 Se7en
#  23 The Silence of the Lambs
#  24 It's a Wonderful Life
#  25 La vita � bella
#  26 The Usual Suspects
#  27 L�on
#  28 Saving Private Ryan
#  29 Sen to Chihiro no kamikakushi
#  30 Coco
#  31 American History X
#  32 C'era una volta il West
#  33 Interstellar
#  34 The Green Mile
#  35 Psycho
#  36 Casablanca
#  37 City Lights
#  38 Intouchables
#  39 Modern Times
#  40 The Pianist
#  41 Raiders of the Lost Ark
#  42 The Departed
#  43 Rear Window
#  44 Terminator 2: Judgment Day
#  45 Back to the Future
#  46 Whiplash
#  47 Gladiator
#  48 The Lion King
#  49 The Prestige
#  50 Memento
#  51 Apocalypse Now
#  52 Alien
#  53 The Great Dictator
#  54 Sunset Blvd.
#  55 Nuovo Cinema Paradiso
#  56 Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb
#  57 Das Leben der Anderen
#  58 Hotaru no haka
#  59 Paths of Glory
#  60 Django Unchained
#  61 The Shining
#  62 WALL�E
#  63 American Beauty
#  64 Mononoke-hime
#  65 The Dark Knight Rises
#  66 Blade Runner 2049
#  67 Oldeuboi
#  68 Witness for the Prosecution
#  69 Aliens
#  70 Once Upon a Time in America
#  71 Das Boot
#  72 Dangal
#  73 Citizen Kane
#  74 Vertigo
#  75 North by Northwest
#  76 Star Wars: Episode VI - Return of the Jedi
#  77 Braveheart
#  78 Reservoir Dogs
#  79 M
#  80 Requiem for a Dream
#  81 Kimi no na wa.
#  82 Taare Zameen Par
#  83 Le fabuleux destin d'Am�lie Poulain
#  84 A Clockwork Orange
#  85 Lawrence of Arabia
#  86 Amadeus
#  87 Double Indemnity
#  88 Eternal Sunshine of the Spotless Mind
#  89 Taxi Driver
#  90 To Kill a Mockingbird
#  91 Full Metal Jacket
#  92 2001: A Space Odyssey
#  93 Singin' in the Rain
#  94 Toy Story
#  95 3 Idiots
#  96 The Sting
#  97 Toy Story 3
#  98 Inglourious Basterds
#  99 Ladri di biciclette
# 100 The Kid
# 101 Snatch
# 102 Monty Python and the Holy Grail
# 103 Good Will Hunting
# 104 Jagten
# 105 Per qualche dollaro in pi�
# 106 Scarface
# 107 L.A. Confidential
# 108 The Apartment
# 109 Metropolis
# 110 Jodaeiye Nader az Simin
# 111 Rash�mon
# 112 Indiana Jones and the Last Crusade
# 113 All About Eve
# 114 Y�jinb�
# 115 Babam ve Oglum
# 116 Up
# 117 Batman Begins
# 118 Some Like It Hot
# 119 The Treasure of the Sierra Madre
# 120 Unforgiven
# 121 Der Untergang
# 122 Die Hard
# 123 Heat
# 124 Raging Bull
# 125 The Third Man
# 126 Bacheha-Ye aseman
# 127 The Great Escape
# 128 Ikiru
# 129 Chinatown
# 130 El laberinto del fauno
# 131 Tonari no Totoro
# 132 Incendies
# 133 Ran
# 134 Judgment at Nuremberg
# 135 The Gold Rush
# 136 El secreto de sus ojos
# 137 Hauru no ugoku shiro
# 138 Inside Out
# 139 On the Waterfront
# 140 The Bridge on the River Kwai
# 141 Det sjunde inseglet
# 142 Room
# 143 Lock, Stock and Two Smoking Barrels
# 144 Mr. Smith Goes to Washington
# 145 A Beautiful Mind
# 146 Casino
# 147 Blade Runner
# 148 Dunkirk
# 149 The Elephant Man
# 150 V for Vendetta
# 151 The Wolf of Wall Street
# 152 Smultronst�llet
# 153 The General
# 154 Warrior
# 155 Dial M for Murder
# 156 Trainspotting
# 157 Gran Torino
# 158 Gone with the Wind
# 159 The Deer Hunter
# 160 The Sixth Sense
# 161 Sunrise: A Song of Two Humans
# 162 Fargo
# 163 No Country for Old Men
# 164 The Thing
# 165 The Big Lebowski
# 166 Finding Nemo
# 167 Andrey Rublev
# 168 T�ky� monogatari
# 169 Eskiya
# 170 There Will Be Blood
# 171 Cool Hand Luke
# 172 Idi i smotri
# 173 Rebecca
# 174 Kill Bill: Vol. 1
# 175 Hacksaw Ridge
# 176 How to Train Your Dragon
# 177 Rang De Basanti
# 178 Mary and Max
# 179 Gone Girl
# 180 La passion de Jeanne d'Arc
# 181 Shutter Island
# 182 Into the Wild
# 183 Life of Brian
# 184 It Happened One Night
# 185 La La Land
# 186 Relatos salvajes
# 187 Logan
# 188 Platoon
# 189 Hotel Rwanda
# 190 Network
# 191 In the Name of the Father
# 192 Le salaire de la peur
# 193 Stand by Me
# 194 Rush
# 195 A Wednesday
# 196 Ben-Hur
# 197 The Grand Budapest Hotel
# 198 Persona
# 199 Les quatre cents coups
# 200 Jurassic Park
# 201 Salinui chueok
# 202 12 Years a Slave
# 203 Mad Max: Fury Road
# 204 Million Dollar Baby
# 205 Spotlight
# 206 Thor: Ragnarok
# 207 Stalker
# 208 The Truman Show
# 209 Amores perros
# 210 Butch Cassidy and the Sundance Kid
# 211 Hachi: A Dog's Tale
# 212 Kaze no tani no Naushika
# 213 Before Sunrise
# 214 The Princess Bride
# 215 The Maltese Falcon
# 216 Prisoners
# 217 Le notti di Cabiria
# 218 Paper Moon
# 219 Harry Potter and the Deathly Hallows: Part 2
# 220 Catch Me If You Can
# 221 Rocky
# 222 The Grapes of Wrath
# 223 Les diaboliques
# 224 Touch of Evil
# 225 Monsters, Inc.
# 226 Gandhi
# 227 Donnie Darko
# 228 Barry Lyndon
# 229 The Terminator
# 230 Annie Hall
# 231 The Bourne Ultimatum
# 232 Groundhog Day
# 233 The Wizard of Oz
# 234 La haine
# 235 8�
# 236 Munna Bhai M.B.B.S.
# 237 Jaws
# 238 The Best Years of Our Lives
# 239 Twelve Monkeys
# 240 Mou gaan dou
# 241 Faa yeung nin wa
# 242 Paris, Texas
# 243 The Help
# 244 Dead Poets Society
# 245 Beauty and the Beast
# 246 Dog Day Afternoon
# 247 Ah-ga-ssi
# 248 Pirates of the Caribbean: The Curse of the Black Pearl
# 249 PK
# 250 Tenk� no shiro Rapyuta

# --------------------------------------------------------------------------------------------------
# ratings.txt
# --------------------------------------------------------------------------------------------------
# Rank  9.2 | ** 2 movies
# Rank  9.0 | ** 2 movies
# Rank  8.9 | **** 4 movies
# Rank  8.8 | *** 3 movies
# Rank  8.7 | ******* 7 movies
# Rank  8.6 | ******** 8 movies
# Rank  8.5 | ************************* 25 movies
# Rank  8.4 | ******************* 19 movies
# Rank  8.3 | ************************************* 37 movies
# Rank  8.2 | ***************************************** 41 movies
# Rank  8.1 | ******************************************************************* 67 movies
# Rank  8.0 | *********************************** 35 movies

# --------------------------------------------------------------------------------------------------
# years.txt
# --------------------------------------------------------------------------------------------------
# Year 1995 | ********* 9 movies
# Year 2003 | ******* 7 movies
# Year 1957 | ******* 7 movies
# Year 2014 | ****** 6 movies
# Year 2009 | ****** 6 movies
# Year 2001 | ****** 6 movies
# Year 2000 | ****** 6 movies
# Year 2017 | ***** 5 movies
# Year 2016 | ***** 5 movies
# Year 2011 | ***** 5 movies
# Year 2010 | ***** 5 movies
# Year 2007 | ***** 5 movies
# Year 2006 | ***** 5 movies
# Year 2004 | ***** 5 movies
# Year 2002 | ***** 5 movies
# Year 1999 | ***** 5 movies
# Year 1998 | ***** 5 movies
# Year 1997 | ***** 5 movies
# Year 1994 | ***** 5 movies
# Year 1984 | ***** 5 movies
# Year 1975 | ***** 5 movies
# Year 2015 | **** 4 movies
# Year 2013 | **** 4 movies
# Year 2008 | **** 4 movies
# Year 1993 | **** 4 movies
# Year 1988 | **** 4 movies
# Year 1986 | **** 4 movies
# Year 1980 | **** 4 movies
# Year 1979 | **** 4 movies
# Year 1959 | **** 4 movies
# Year 1954 | **** 4 movies
# Year 2012 | *** 3 movies
# Year 2005 | *** 3 movies
# Year 1996 | *** 3 movies
# Year 1991 | *** 3 movies
# Year 1985 | *** 3 movies
# Year 1982 | *** 3 movies
# Year 1976 | *** 3 movies
# Year 1966 | *** 3 movies
# Year 1950 | *** 3 movies
# Year 1940 | *** 3 movies
# Year 1939 | *** 3 movies
# Year 1992 | ** 2 movies
# Year 1989 | ** 2 movies
# Year 1987 | ** 2 movies
# Year 1983 | ** 2 movies
# Year 1981 | ** 2 movies
# Year 1977 | ** 2 movies
# Year 1974 | ** 2 movies
# Year 1973 | ** 2 movies
# Year 1968 | ** 2 movies
# Year 1963 | ** 2 movies
# Year 1962 | ** 2 movies
# Year 1961 | ** 2 movies
# Year 1960 | ** 2 movies
# Year 1958 | ** 2 movies
# Year 1953 | ** 2 movies
# Year 1952 | ** 2 movies
# Year 1948 | ** 2 movies
# Year 1946 | ** 2 movies
# Year 1941 | ** 2 movies
# Year 1931 | ** 2 movies
# Year 1927 | ** 2 movies
# Year 1990 | * 1 movie
# Year 1978 | * 1 movie
# Year 1972 | * 1 movie
# Year 1971 | * 1 movie
# Year 1969 | * 1 movie
# Year 1967 | * 1 movie
# Year 1965 | * 1 movie
# Year 1964 | * 1 movie
# Year 1955 | * 1 movie
# Year 1949 | * 1 movie
# Year 1944 | * 1 movie
# Year 1942 | * 1 movie
# Year 1936 | * 1 movie
# Year 1934 | * 1 movie
# Year 1928 | * 1 movie
# Year 1926 | * 1 movie
# Year 1925 | * 1 movie
# Year 1921 | * 1 movie
