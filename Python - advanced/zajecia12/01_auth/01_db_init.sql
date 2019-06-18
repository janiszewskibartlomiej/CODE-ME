DROP TABLE IF EXISTS "users";

CREATE TABLE "users"
(
    "id"       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "username" TEXT    NOT NULL,
    "password" TEXT    NOT NULL
);

INSERT INTO "users"
VALUES (NULL, 'testowy', 'haslo');
