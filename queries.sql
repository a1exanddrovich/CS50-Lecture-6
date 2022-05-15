SELECT COUNT(title) FROM favs WHERE title LIKE "%office%";

SELECT title FROM favs WHERE title = "Thevoffice";

UPDATE title SET title = "The office" WHERE title = "Thevoffice";

SELECT genres FROM favs;

SELECT title FROM favs WHERE genres = "Comedy";

SELECT title FROM favs WHERE genres LIKE "%Comedy%";

CREATE TABLE shows (id INTEGER, title TEXT NOT NULL, PRIMARY KEY(id));

CREATE TABLE genres (show_id INTEGER, genre TEXT NOT NULL , FOREIGN KEY(show_id) REFERENCES shows(id));

SELECT show_id FROM genres WHERE genre = "Comedy";

SELECT DISTINCT title FROM shows WHERE id IN (SELECT show_id FROM genres WHERE genre = "Comedy");

INSERT INTO shows (title) VALUES ("Seinfeld");
INSERT INTO genres (show_id, genre) VALUES ((SELECT id FROM shows WHERE title = "Seinfeld"), "Comedy");
