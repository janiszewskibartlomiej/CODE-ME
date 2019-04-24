DROP TABLE IF EXISTS "produkty";

CREATE TABLE "produkty"
(
    "id"        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "nazwa"     TEXT,
    "cena"      REAL,
    "jednostka" TEXT,
    "promocja"  INTEGER DEFAULT 0
);

INSERT INTO "produkty"
VALUES (NULL, 'Mleko Świeże 2%', 1.99, 'op', 1),
       (NULL, 'Karkówka bez kości', 8.99, 'kg', 1),
       (NULL, 'Twaróg sernikowy 1000g', 5.99, 'op', 1),
       (NULL, 'Ser w plasterkach', 5.49, 'op', 0),
       (NULL, 'Herbata torebki 200g', 9.99, 'op', 0),
       (NULL, 'Cytryny', 7.99, 'kg', 0),
       (NULL, 'Gruszki', 2.99, 'kg', 1),
       (NULL, 'Czekolada', 2.49, 'op', 1);
