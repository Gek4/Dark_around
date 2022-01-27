import sqlite3

# Програмка для заполнения таблицы

con = sqlite3.connect('Rating_of_the_game.db')
cur = con.cursor()


def add_in_db(number, nickname, time):
    cur.execute(f"""Insert Into rating(number, nickname, time) values('{number}', '{nickname}', '{time}')""").fetchall()
    con.commit()
    con.close()
