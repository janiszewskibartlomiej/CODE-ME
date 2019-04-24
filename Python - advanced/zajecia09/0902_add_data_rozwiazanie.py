import sqlite3

conn = sqlite3.connect('zadanie09_baza.db')

c = conn.cursor()

zapytanie = """
INSERT INTO 'zwierzaki' 
VALUES (NULL, 'Filemon', 'kot', 0.5),
        (NULL, 'Bonifacy', 'kot', 12),
        (NULL, 'Reksio', 'pies', 3),
        (NULL, 'Garfield', 'kot', 8),
        (NULL, 'Pluto', 'pies', 5);
"""

c.execute(zapytanie)

conn.commit()
conn.close()
