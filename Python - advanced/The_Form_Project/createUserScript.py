import sqlite3
import hashlib

conn = sqlite3.connect('questionDataBase.db')

c = conn.cursor()

zapytanie = """

    INSERT INTO "login" ("id", "user", "password", "admin") 
    
    VALUES (NULL, ?, ?, ?)"""
login = input('Wpisz login: ')

haslo = input('Wpisz hasło: ')
haslo = haslo.encode()
haslo = hashlib.sha256(haslo)
haslo = haslo.digest()
print(haslo)

admin = input('Czy użytkownik ma mieć uprawnienia "Admin" [T lub N]: ')
if admin == 'T' or 't':
    admin = 'true'
else:
    admin = 'false'

c.execute(zapytanie, (login, haslo, admin))

conn.commit()

conn.close()
