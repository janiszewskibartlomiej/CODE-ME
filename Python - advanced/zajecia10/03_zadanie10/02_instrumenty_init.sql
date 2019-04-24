CREATE TABLE "instrumenty"
(
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "muzyk_id" INTEGER,
    "instrument" TEXT,
    FOREIGN KEY ("muzyk_id") REFERENCES "beatles" ("id")
);

INSERT INTO "instrumenty"
VALUES (NULL, 1, 'wokal'),
       (NULL, 1, 'gitara'),
       (NULL, 1, 'pianino'),
       (NULL, 1, 'harmonijka ustna'),
       (NULL, 2, 'wokal'),
       (NULL, 2, 'bas'),
       (NULL, 2, 'gitara'),
       (NULL, 2, 'pianino'),
       (NULL, 3, 'gitara'),
       (NULL, 3, 'wokal'),
       (NULL, 3, 'gitara'),
       (NULL, 3, 'pianino'),
       (NULL, 4, 'perkusja'),
       (NULL, 4, 'wokal');

