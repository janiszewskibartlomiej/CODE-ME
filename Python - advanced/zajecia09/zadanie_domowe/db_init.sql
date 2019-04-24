DROP TABLE IF EXISTS 'plecak';

CREATE TABLE 'plecak' (
    'id'	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    'nazwa'	TEXT NOT NULL,
    'rodzaj' INTEGER CHECK (rodzaj IN ('sprzet', 'jedzenie')),
    'ilosc'	INTEGER DEFAULT 1,
    'waga'	INTEGER
);

INSERT INTO 'plecak' VALUES (NULL, 'Szczoteczka do zębów', 'sprzet', 1, 0.08);
INSERT INTO 'plecak' VALUES (NULL, 'Skarpety', 'sprzet', 4, 0.06);
INSERT INTO 'plecak' VALUES (NULL, 'Wafelek czekoladowy', 'jedzenie', 6, 0.17);
INSERT INTO 'plecak' VALUES (NULL, 'Latarka czołowa', 'sprzet', 1, 0.1);
