CREATE TABLE "beatles"
(
    "id"       INTEGER NOT NULL PRIMARY KEY UNIQUE,
    "imie"     TEXT,
    "nazwisko" TEXT    NOT NULL
);

INSERT INTO "beatles"
VALUES (1, 'John', 'Lennon'),
       (2, 'Paul', 'McCartney'),
       (3, 'George', 'Harrison'),
       (4, 'Ringo', 'Starr');
