PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS "data";
DROP TABLE IF EXISTS "users";

CREATE TABLE "users"
(
    "id"       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "username" TEXT    NOT NULL,
    "password" TEXT    NOT NULL,
    "is_admin" BOOLEAN NOT NULL
);

INSERT INTO "users"
VALUES (1, 'pat', 'pbkdf2:sha256:150000$4LgSdQVe$ac680c759dd12895c101c6757f86d4f383588b6d4968866c6844562d0ce66187', 0),
       (2, 'mat', 'pbkdf2:sha256:150000$4LgSdQVe$ac680c759dd12895c101c6757f86d4f383588b6d4968866c6844562d0ce66187', 0),
       (3, 'b1111', 'pbkdf2:sha256:150000$LvYfLNU7$149f17012d69851735e784a994518ab7dc4a0d51bb7c8f9f4e8105cfde5b2ef7', 1);


CREATE TABLE "data"
(
    "id"      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "user_id" INTEGER NOT NULL,
    "nazwa"   TEXT    NOT NULL,
    FOREIGN KEY ("user_id") REFERENCES "users" ("id")
);

INSERT INTO "data"
VALUES (NULL, 1, 'wiertarka'),
       (NULL, 1, 'młotek'),
       (NULL, 1, 'gwoździe'),
       (NULL, 2, 'taczka'),
       (NULL, 2, 'drabina'),
       (NULL, 2, 'śrubokręt'),
       (NULL, 1, 'worek cementu');
