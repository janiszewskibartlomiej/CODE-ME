import sqlite3

conn = sqlite3.connect('questionDataBase.db')

c = conn.cursor()

zapytanie1 = """
    DROP TABLE IF EXISTS 'login';

    CREATE TABLE "login" (
    "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "user"	TEXT NOT NULL UNIQUE ,
    "password"	TEXT NOT NULL,
    "admin" TEXT NOT NULL);
    """
c.executescript(zapytanie1)

conn.commit()
# conn.close()

zapytanie2 = """
    DROP TABLE IF EXISTS 'questions';
    
    CREATE TABLE "questions" (
    "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "id_user"	INTEGER NOT NULL,
    "question"	TEXT,
    "type" TEXT NOT NULL);
    """
c.executescript(zapytanie2)

zapytanie3 = """
    DROP TABLE IF EXISTS 'answers';
    
    CREATE TABLE "answers" (
    "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "id_user"	INTEGER NOT NULL,
    "id_question"	INTEGER NOT NULL,
    "answer" TEXT NOT NULL,
    "is_answer" TEXT);
    """
c.executescript(zapytanie3)

conn.commit()
conn.close()
