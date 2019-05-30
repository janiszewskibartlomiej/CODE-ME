import sqlite3
from createAdminAccount import create_admin

conn = sqlite3.connect('questionDataBase.db')
c = conn.cursor()


def wykonaj_skrypt_sql(skrypt):
    with open(skrypt, encoding='utf-8') as f:
        zapytanie = f.read()
    c.executescript(zapytanie)


wykonaj_skrypt_sql('data_sql_creating.sql')

conn.commit()
conn.close()

if __name__ == '__main__':
    create_admin()
