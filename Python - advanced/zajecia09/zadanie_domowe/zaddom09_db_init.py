import sqlite3

conn = sqlite3.connect('zaddom09.db')
c = conn.cursor()

with open('db_init.sql', encoding='utf-8') as f:
    skrypt = f.read()

c.executescript(skrypt)

conn.commit()
conn.close()
