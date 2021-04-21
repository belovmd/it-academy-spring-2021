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
    # Функция возвращает словарь типа:
    # {Порядковый_№_фильма: [Название, год, рейтинг]}

    dict_top_250 = dict()
    index = 1
    try:
        with open('ratings.list', 'r') as rating_list:

            while len(dict_top_250) != 250:
                line = rating_list.readline()
                formatted_line = line.strip().split()
                if formatted_line and formatted_line[0].isdigit() and len(formatted_line[0]) == 10:
                    dict_top_250[index] = [' '.join(formatted_line[3:-1]),
                                           int(formatted_line[-1][1:5]),
                                           float(formatted_line[2])]
                    index += 1
        return dict_top_250
    except FileNotFoundError:
        print('File Not Found')


def create_top_250():
    # Функция создает и наполняет
    # списком фильмов файл top250_movies.txt

    with open('top250_movies.txt', 'w') as file_:
        index = 1
        for film in (dict_top250().values()):
            file_.writelines('{}. {}\n'.format(index, film[0]))
            index += 1


def create_bar_graph_rating():
    # Функция создает гистограмму
    # рейтинга фильмов и записывает ее
    # в файл ratings.txt

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
    # Функция создает гистограмму
    # годов выпуска фильмов и записывает ее
    # в файл years.txt

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

"""
top250_movies.txt
1. The Shawshank Redemption
2. The Godfather
3. The Godfather: Part II
4. The Dark Knight
5. 12 Angry Men
6. Schindler's List
7. Pulp Fiction
8. The Lord of the Rings: The Return of the King
9. Il buono, il brutto, il cattivo
10. Fight Club
11. The Lord of the Rings: The Fellowship of the Ring
12. Forrest Gump
13. Star Wars: Episode V - The Empire Strikes Back
14. Inception
15. The Lord of the Rings: The Two Towers
16. One Flew Over the Cuckoo's Nest
17. Goodfellas
18. The Matrix
19. Shichinin no samurai
20. Star Wars
21. Cidade de Deus
22. Se7en
23. The Silence of the Lambs
24. It's a Wonderful Life
25. La vita и bella
26. The Usual Suspects
27. Lйon
28. Saving Private Ryan
29. Sen to Chihiro no kamikakushi
30. Coco
31. American History X
32. C'era una volta il West
33. Interstellar
34. The Green Mile
35. Psycho
36. Casablanca
37. City Lights
38. Intouchables
39. Modern Times
40. The Pianist
41. Raiders of the Lost Ark
42. The Departed
43. Rear Window
44. Terminator 2: Judgment Day
45. Back to the Future
46. Whiplash
47. Gladiator
48. The Lion King
49. The Prestige
50. Memento
51. Apocalypse Now
52. Alien
53. The Great Dictator
54. Sunset Blvd.
55. Nuovo Cinema Paradiso
56. Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb
57. Das Leben der Anderen
58. Hotaru no haka
59. Paths of Glory
60. Django Unchained
61. The Shining
62. WALL·E
63. American Beauty
64. Mononoke-hime
65. The Dark Knight Rises
66. Blade Runner 2049
67. Oldeuboi
68. Witness for the Prosecution
69. Aliens
70. Once Upon a Time in America
71. Das Boot
72. Dangal
73. Citizen Kane
74. Vertigo
75. North by Northwest
76. Star Wars: Episode VI - Return of the Jedi
77. Braveheart
78. Reservoir Dogs
79. M
80. Requiem for a Dream
81. Kimi no na wa.
82. Taare Zameen Par
83. Le fabuleux destin d'Amйlie Poulain
84. A Clockwork Orange
85. Lawrence of Arabia
86. Amadeus
87. Double Indemnity
88. Eternal Sunshine of the Spotless Mind
89. Taxi Driver
90. To Kill a Mockingbird
91. Full Metal Jacket
92. 2001: A Space Odyssey
93. Singin' in the Rain
94. Toy Story
95. 3 Idiots
96. The Sting
97. Toy Story 3
98. Inglourious Basterds
99. Ladri di biciclette
100. The Kid
101. Snatch
102. Monty Python and the Holy Grail
103. Good Will Hunting
104. Jagten
105. Per qualche dollaro in piщ
106. Scarface
107. L.A. Confidential
108. The Apartment
109. Metropolis
110. Jodaeiye Nader az Simin
111. Rashфmon
112. Indiana Jones and the Last Crusade
113. All About Eve
114. Yфjinbф
115. Babam ve Oglum
116. Up
117. Batman Begins
118. Some Like It Hot
119. The Treasure of the Sierra Madre
120. Unforgiven
121. Der Untergang
122. Die Hard
123. Heat
124. Raging Bull
125. The Third Man
126. Bacheha-Ye aseman
127. The Great Escape
128. Ikiru
129. Chinatown
130. El laberinto del fauno
131. Tonari no Totoro
132. Incendies
133. Ran
134. Judgment at Nuremberg
135. The Gold Rush
136. El secreto de sus ojos
137. Hauru no ugoku shiro
138. Inside Out
139. On the Waterfront
140. The Bridge on the River Kwai
141. Det sjunde inseglet
142. Room
143. Lock, Stock and Two Smoking Barrels
144. Mr. Smith Goes to Washington
145. A Beautiful Mind
146. Casino
147. Blade Runner
148. Dunkirk
149. The Elephant Man
150. V for Vendetta
151. The Wolf of Wall Street
152. Smultronstдllet
153. The General
154. Warrior
155. Dial M for Murder
156. Trainspotting
157. Gran Torino
158. Gone with the Wind
159. The Deer Hunter
160. The Sixth Sense
161. Sunrise: A Song of Two Humans
162. Fargo
163. No Country for Old Men
164. The Thing
165. The Big Lebowski
166. Finding Nemo
167. Andrey Rublev
168. Tфkyф monogatari
169. Eskiya
170. There Will Be Blood
171. Cool Hand Luke
172. Idi i smotri
173. Rebecca
174. Kill Bill: Vol. 1
175. Hacksaw Ridge
176. How to Train Your Dragon
177. Rang De Basanti
178. Mary and Max
179. Gone Girl
180. La passion de Jeanne d'Arc
181. Shutter Island
182. Into the Wild
183. Life of Brian
184. It Happened One Night
185. La La Land
186. Relatos salvajes
187. Logan
188. Platoon
189. Hotel Rwanda
190. Network
191. In the Name of the Father
192. Le salaire de la peur
193. Stand by Me
194. Rush
195. A Wednesday
196. Ben-Hur
197. The Grand Budapest Hotel
198. Persona
199. Les quatre cents coups
200. Jurassic Park
201. Salinui chueok
202. 12 Years a Slave
203. Mad Max: Fury Road
204. Million Dollar Baby
205. Spotlight
206. Thor: Ragnarok
207. Stalker
208. The Truman Show
209. Amores perros
210. Butch Cassidy and the Sundance Kid
211. Hachi: A Dog's Tale
212. Kaze no tani no Naushika
213. Before Sunrise
214. The Princess Bride
215. The Maltese Falcon
216. Prisoners
217. Le notti di Cabiria
218. Paper Moon
219. Harry Potter and the Deathly Hallows: Part 2
220. Catch Me If You Can
221. Rocky
222. The Grapes of Wrath
223. Les diaboliques
224. Touch of Evil
225. Monsters, Inc.
226. Gandhi
227. Donnie Darko
228. Barry Lyndon
229. The Terminator
230. Annie Hall
231. The Bourne Ultimatum
232. Groundhog Day
233. The Wizard of Oz
234. La haine
235. 8Ѕ
236. Munna Bhai M.B.B.S.
237. Jaws
238. The Best Years of Our Lives
239. Twelve Monkeys
240. Mou gaan dou
241. Faa yeung nin wa
242. Paris, Texas
243. The Help
244. Dead Poets Society
245. Beauty and the Beast
246. Dog Day Afternoon
247. Ah-ga-ssi
248. Pirates of the Caribbean: The Curse of the Black Pearl
249. PK
250. Tenkы no shiro Rapyuta
"""

"""
ratings.txt
8.0 : ***********************************
8.1 : *******************************************************************
8.2 : *****************************************
8.3 : *************************************
8.4 : *******************
8.5 : *************************
8.6 : ********
8.7 : *******
8.8 : ***
8.9 : ****
9.0 : **
9.2 : **
"""

"""
years.txt
1921 : *
1925 : *
1926 : *
1927 : **
1928 : *
1931 : **
1934 : *
1936 : *
1939 : ***
1940 : ***
1941 : **
1942 : *
1944 : *
1946 : **
1948 : **
1949 : *
1950 : ***
1952 : **
1953 : **
1954 : ****
1955 : *
1957 : *******
1958 : **
1959 : ****
1960 : **
1961 : **
1962 : **
1963 : **
1964 : *
1965 : *
1966 : ***
1967 : *
1968 : **
1969 : *
1971 : *
1972 : *
1973 : **
1974 : **
1975 : *****
1976 : ***
1977 : **
1978 : *
1979 : ****
1980 : ****
1981 : **
1982 : ***
1983 : **
1984 : *****
1985 : ***
1986 : ****
1987 : **
1988 : ****
1989 : **
1990 : *
1991 : ***
1992 : **
1993 : ****
1994 : *****
1995 : *********
1996 : ***
1997 : *****
1998 : *****
1999 : *****
2000 : ******
2001 : ******
2002 : *****
2003 : *******
2004 : *****
2005 : ***
2006 : *****
2007 : *****
2008 : ****
2009 : ******
2010 : *****
2011 : *****
2012 : ***
2013 : ****
2014 : ******
2015 : ****
2016 : *****
2017 : *****
"""
