import sqlite3
import hashlib
from werkzeug.security import generate_password_hash

conn = sqlite3.connect('questionDataBase.db')

c = conn.cursor()

zapytanie = """

    INSERT INTO "login" ("id", "user", "password", "admin") 
    
    VALUES (NULL, ?, ?, ?)"""

login = input('Wpisz login: ')

haslo = input('Wpisz hasło: ')

haslo_sha = generate_password_hash(haslo)



# haslo = haslo.encode()
# haslo = hashlib.sha256(haslo)
# haslo = haslo.digest()
print('Hasło: ', haslo, haslo_sha)

admin = 'true'

# admin = input('Czy użytkownik ma mieć uprawnienia "Admin" [T lub N]: ')
# if admin == 'T' or 't':
#     admin = 'true'
# else:
#     admin = 'false'

c.execute(zapytanie, (login, haslo_sha, admin))

conn.commit()

conn.close()
