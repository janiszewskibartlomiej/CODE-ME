PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS "data";
DROP TABLE IF EXISTS "users";

CREATE TABLE "users"
(
    "id"       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "username" TEXT    NOT NULL,
    "password" TEXT    NOT NULL,
    "is_admin" BOOLEAN NOT NULL DEFAULT 0
);

INSERT INTO "users"
VALUES (1, 'pat', 'pbkdf2:sha256:150000$INXfG3hk$682e0ac6eb6493893238553678a142e3c76b2dc37df4c5582f0ff01f408eb895', 0),
       (2, 'mat', 'pbkdf2:sha256:150000$7rOWWKhb$890166da0eb1dbf4f87353ea013487d113cdafc9473c80cea2f93af786851e16', 0),
       (3, 'admin', 'pbkdf2:sha256:150000$7rOWWKhb$890166da0eb1dbf4f87353ea013487d113cdafc9473c80cea2f93af786851e16',
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
