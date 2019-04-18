import sqlite3

conn = sqlite3.connect('loginDataBase.db')

c = conn.cursor()

zapytanie = """
    DROP TABLE IF EXISTS 'login';
    
    CREATE TABLE "login" (
    "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "user"	TEXT,
    "password"	TEXT,
    "admin" TEXT);
    """
c.executescript(zapytanie)

conn.commit()
conn.close()
