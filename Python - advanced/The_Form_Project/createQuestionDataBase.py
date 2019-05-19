import sqlite3

conn = sqlite3.connect('questionDataBase.db')

c = conn.cursor()

zapytanie1 = """
    DROP TABLE IF EXISTS 'login';

    CREATE TABLE "login" (
    "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "user"	TEXT UNIQUE,
    "password"	TEXT,
    "admin" TEXT);
    """
c.executescript(zapytanie1)

conn.commit()
# conn.close()

zapytanie2 = """
    DROP TABLE IF EXISTS 'questions';
    
    CREATE TABLE "questions" (
    "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "tworca"	TEXT,
    "pytanie"	TEXT,
    "typ" TEXT);
    """
c.executescript(zapytanie2)

conn.commit()
conn.close()
