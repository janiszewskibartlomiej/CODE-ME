CREATE TABLE "zespoly"
(
    "id"            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "nazwa"         TEXT    NOT NULL,
    "rok_zalozenia" INTEGER NOT NULL
);

INSERT INTO "zespoly"
VALUES (1, 'The Beatles', 1960),
       (2, 'Queen', 1970),
       (3, 'Lady Pank', 1981),
       (4, 'Nowy Zespół', 2020)
