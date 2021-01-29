

CREATE TABLE Bands(
	band_id       SERIAL,
	band_URL      VARCHAR(150) NOT NULL,
	band_name     VARCHAR(70)  NOT NULL,
	PRIMARY KEY (band_id),
    UNIQUE(band_URL)
);


CREATE TABLE Genres(
	genre_id SERIAL,
	genre    VARCHAR(100)  NOT NULL,
	PRIMARY KEY(genre_id),
    UNIQUE(genre)
);


CREATE TABLE Bands_Genres(
	band_id     INTEGER ,
	genre_id    INTEGER,
	PRIMARY KEY(band_id,genre_id),
    FOREIGN KEY (band_id) REFERENCES Bands, 
    FOREIGN KEY (genre_id) REFERENCES Genres
);

CREATE TABLE Artists(
    artist_id    SERIAL,
    artist_url   VARCHAR(150) NOT NULL,
    PRIMARY KEY (artist_id),
    UNIQUE(artist_url)
);

CREATE TABLE Albums(
    album_id     SERIAL,
	band_id      INTEGER,
	album_name   VARCHAR(140) NOT NULL,
	release      DATE         NOT NULL,
	sales        INTEGER,
	time         FLOAT        NOT NULL,
	abstract     TEXT,
	PRIMARY KEY(album_id),
    UNIQUE(band_id,album_name,release,sales,time),
	FOREIGN KEY(band_id) REFERENCES Bands
);

CREATE TABLE Belongs(
	band_id         INTEGER,
    artist_id       INTEGER,
    artist_name     VARCHAR(150)   NOT NULL,
	is_active		BOOLEAN        NOT NULL,
    PRIMARY KEY (band_id, artist_id, artist_name),
    FOREIGN KEY (artist_id) REFERENCES Artists,
	FOREIGN KEY (band_id) REFERENCES Bands
);

--copy the data

\copy Bands( band_URL, band_name) from '../new_sets/Bands.csv' DELIMITER ';' CSV HEADER;

\copy Genres( genre) from '../new_sets/Genres.csv' DELIMITER ';'  CSV HEADER;

\copy Bands_Genres(band_id, genre_id) from '../new_sets/Bands_Genres.csv' DELIMITER ';' CSV HEADER;

\copy Artists(artist_url) from '../new_sets/Artists.csv' DELIMITER ';' CSV HEADER;



\copy Albums(band_id, album_name, release, sales, time, abstract) from '../new_sets/Albums.csv' DELIMITER ';' CSV HEADER;


\copy Belongs(band_id, artist_id, artist_name, is_active) from '../new_sets/Belongs.csv' DELIMITER ';' CSV HEADER;



