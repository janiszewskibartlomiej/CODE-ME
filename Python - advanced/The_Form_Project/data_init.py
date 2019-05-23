import sqlite3
from createAdminScript import create_admin

conn = sqlite3.connect('questionDataBase.db')
c = conn.cursor()


def wykonaj_skrypt_sql(skrypt):
    with open(skrypt, encoding='utf-8') as f:
        zapytanie = f.read()
    c.executescript(zapytanie)


wykonaj_skrypt_sql('create_data.sql')

conn.commit()
conn.close()

create_admin()
