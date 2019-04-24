CREATE TABLE "muzycy"
(
    "id"         INTEGER NOT NULL PRIMARY KEY UNIQUE,
    "zespol_id"     INTEGER NOT NULL,
    "imie"       TEXT,
    "nazwisko"   TEXT    NOT NULL,
    "instrument" TEXT,
    FOREIGN KEY ("zespol_id") REFERENCES "zespoly" ("id")
);

INSERT INTO "muzycy"
VALUES (1, 1, 'John', 'Lennon', 'gitara'),
       (2, 1, 'Paul', 'McCartney', 'bas'),
       (3, 1, 'George', 'Harrison', 'gitara'),
       (4, 1, 'Ringo', 'Starr', 'perkusja'),
       (5, 2, 'Freddie', 'Mercury', 'wokal'),
       (6, 2, 'Brian', 'May', 'gitara'),
       (7, 2, 'John', 'Deacon', 'bas'),
       (8, 2, 'Roger', 'Taylor', 'perkusja'),
       (9, 3, 'Jan', 'Borysewicz', 'gitara'),
       (10, 3, 'Janusz', 'Panasewicz', 'wokal'),
       (11, 3, 'Krzysztof', 'Kieliszkiewicz', 'bas'),
       (12, 3, 'Kuba', 'Jabłoński', 'perkusja');
