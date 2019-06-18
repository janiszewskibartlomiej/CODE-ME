PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS "data";
DROP TABLE IF EXISTS "users";

CREATE TABLE "users"
(
    "id"       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "username" TEXT    NOT NULL,
    "password" TEXT    NOT NULL,
    "is_admin" BOOLEAN NOT NULL DEFAULT FALSE
);

INSERT INTO "users"
VALUES (1, 'pat', 'pbkdf2:sha256:150000$INXfG3hk$682e0ac6eb6493893238553678a142e3c76b2dc37df4c5582f0ff01f408eb895', 0),
       (2, 'mat', 'pbkdf2:sha256:150000$mbSC4jB7$7061b7a1d74a89fa332e48642d45f4d38c44040a3dad788680a2a22935eed192', 0),
       (3, 'admin', 'pbkdf2:sha256:150000$FcdQ2VTw$6c7485e49cf49efd0852895876c53ba5bf31dc73132c4b1bf39ef8f67f0270b0',
        1);


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
