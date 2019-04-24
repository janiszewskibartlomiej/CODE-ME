import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_drop_and_create.py`

conn = sqlite3.connect('baza.db')
c = conn.cursor()

# Żeby użyć wartości domyślnych, lub automatycznie przydzielanych, trzeba użyć NULL
zapytanie = """
INSERT INTO 'produkty' VALUES (NULL, 'Herbata torebki 200g', 9.99, 'op', NULL);
"""

c.execute(zapytanie)

conn.commit()
conn.close()
