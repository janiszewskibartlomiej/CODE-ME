import sqlite3

conn = sqlite3.connect('zadanie09_baza.db')

c = conn.cursor()

zapytanie = """
    INSERT INTO 'zwierzaki' ('imie', 'gatunek', 'wiek') 
    VALUES 
    ('filemon', 'kot',0.5),
    ('bonifacy', 'kot', 12),
    ('reksio', 'pies' , 3),
    ('garfield', 'kot', 8),
    ('pluto', 'pies', 5);
"""

c.execute(zapytanie)

conn.commit()
conn.close()
