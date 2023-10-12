
DROP TABLE IF EXISTS albums CASCADE;
DROP SEQUENCE IF EXISTS albums_id_seq CASCADE;
DROP TABLE IF EXISTS artists CASCADE;
DROP SEQUENCE IF EXISTS artists_id_seq CASCADE;

CREATE SEQUENCE IF NOT EXISTS artists_id_seq;
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name text,
    genre text
);

CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int,
    artist_id int,
    constraint fk_artist foreign key(artist_id) references artists(id)
    on delete cascade
);

INSERT INTO artists (name, genre) VALUES ('Red Hot Chili Peppers', 'Rock');
INSERT INTO artists (name, genre) VALUES ('Nirvana', 'Grunge');
INSERT INTO artists (name, genre) VALUES ('Pearl Jam', 'Grunge');


INSERT INTO albums (title, release_year, artist_id) VALUES ('Californication', 1999, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Nevermind', 1991, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('In Utero', 1993, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Ten', 1991, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('By the Way', 2002, 1);