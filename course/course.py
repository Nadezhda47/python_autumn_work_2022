# Предметная область: БД для магазина музыкальных произведений. Покупатели самостоятельно находят и выбирают понравившийся у них товар

# 1. Концепция
# Выделены сущности: Композитор, Альбом, Произведение
# Смысл: Исполнитель записывает произведения, которые объединяются в альбомы

# 2. Логическая модель:

    # Исполнитель (music_artist)
    # id (число)
    # Композитор (строка)
    # Описание (текст)
    # Жанр (строка)
    # Страна (текст)

    # Альбом:
    # id (число)
    # Название (строка)
    # Описание (текст)
    # Жанр (строка)
    # Год выпуска (число)
    # Лейбл (строка)
    # Носитель (строка)

    # Произведение:
    # id (число)
    # Название (строка)
    # Исполнитель (строка)
    # Год выпуска (число)

    # Склад
    # id (число)
    # Наименование альбома (строка)
    # Носитель
    # Ячейка (текст)

# Анализ связи:

# Исполнитель 1 : n Альбом
# Исполнитель n : n Произведение
# Альбом  n : n Произведение
# Альбом n : n Склад

# 3. Физическая модель
# https://editor.ponyorm.com/user/Nadezhda47/Course/designer

# 4. Запросы к базе данных

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="m_s",
    user="postgres",
    password="1234")
cur = conn.cursor()

# 1. Показать все произведения данного композитора (исполнителя), имеющиеся в магазине
id_artist = input("Введите исполнителя")
print("Все произведения данного композитора (исполнителя), имеющиеся в магазине")
SQL_GET_TASK_BY_ARTIST = f"""select m.artist_name, c.music_track
                         FROM music_artist m, composition c, artist_track at2
                         where m.id = at2.id_music_artist
                         and at2.id_composition = c.id
                         and m.artist_name = '{id_artist}'"""

cur.execute(SQL_GET_TASK_BY_ARTIST)
records = cur.fetchall()
for row in records:
    print(row)

# 2. Показать местоположение выбранного произведения;
composition = input("Введите произведение ")
print("местоположение выбранного произведения")
SQL_GET_TASK_BY_LOCAION = f"""select c.music_track, a."location", a.media_type
                          FROM composition c, composition_album ca, album a
                          where c.id = ca.id_composition
                          and ca.id_album = a.id
                          and c.music_track  = '{composition}'"""

cur.execute(SQL_GET_TASK_BY_LOCAION)
records = cur.fetchall()
for row in records:
    print(row)

# 3. Показать список носителей для выбранного произведения
print("список носителей для выбранного произведения")

SQL_GET_TASK_BY_TYPE = f"""select c.music_track, a.media_type
                       FROM composition c, composition_album ca, album a
                       where c.id = ca.id_composition
                       and ca.id_album = a.id
                       and c.music_track  = '{composition}'"""

cur.execute(SQL_GET_TASK_BY_TYPE)
records = cur.fetchall()
for row in records:
    print(row)

# 4. Показать список произведений по жанру исполнения;

genre = input("Введите жанр ")
print("список произведений по жанру исполнения")

SQL_GET_TASK_BY_GENRE = f"""select c.music_track, a.genre
                        FROM composition c, composition_album ca, album a
                        where c.id = ca.id_composition
                        and ca.id_album = a.id
                        and a.genre  = '{genre}'"""

cur.execute(SQL_GET_TASK_BY_GENRE)
records = cur.fetchall()
for row in records:
    print(row)

# 5. Находить произведение по названию, году выпуска, альбому и т.д.

track = input("Введите произведение ")
year = int(input("Введите год"))
album = input("Введите название альбома (указать в одинарных кавычках)")
print("произведение по названию, году выпуска, альбому и т.д.")

SQL_GET_TASK_BY_MASS = f"""select c.music_track, a.album_title
                        FROM composition c, composition_album ca, album a
                        where c.id = ca.id_composition
                        and ca.id_album = a.id
                        and c.music_track  = '{track}'
                        or a.release_year = '{year}'
                        or a.album_title = '{album}'
                        GROUP by c.music_track, a.album_title
                        order by a.album_title"""

cur.execute(SQL_GET_TASK_BY_MASS)
records = cur.fetchall()
for row in records:
    print(row)

# 6. Показывать список произведений данного композитора (исполнителя) по выбранным годам творчества.

artist_two = input("Введите исполнителя ")
year_two = int(input("Введите год"))
print("список произведений данного композитора (исполнителя) по выбранным годам творчества")

SQL_GET_TASK_BY_YEAR = f"""select m.artist_name, c.music_track, a.release_year 
                           FROM music_artist m, composition c, artist_track at2, album a, composition_album ca 
                           where m.id = at2.id_music_artist 
                           and at2.id_composition = c.id 
                           and c.id = ca.id_composition 
                           and ca.id_album = a.id 
                           and m.artist_name = '{artist_two}' 
                           and a.release_year = '{year_two}'
                           GROUP by c.music_track, m.artist_name, a.release_year """

cur.execute(SQL_GET_TASK_BY_YEAR)
records = cur.fetchall()
for row in records:
    print(row)

#db.conn(close)
