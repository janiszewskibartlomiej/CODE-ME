import sqlite3

conn = sqlite3.connect('baza.db')
c = conn.cursor()


def wykonaj_skrypt_sql(skrypt):
    with open(skrypt, encoding='utf-8') as f:
        zapytanie = f.read()
    c.executescript(zapytanie)


wykonaj_skrypt_sql('00_drop_tables.sql')
wykonaj_skrypt_sql('01_zespoly_init.sql')
wykonaj_skrypt_sql('02_muzycy_init.sql')

conn.commit()

conn.close()
