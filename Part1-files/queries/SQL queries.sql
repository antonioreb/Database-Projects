
--Query1: Which artists have belonged or belong to the Indie Rock band which has releasedthe longest albuns, on average?

CREATE VIEW Bands_Average AS SELECT A.band_id AS band_id, AVG(A.time) AS avg_lenght  --3
      			  FROM Albums A
      			  GROUP BY A.band_id
			      HAVING A.band_id IN (SELECT BA.band_id            --4
					       FROM Bands BA, Bands_Genres BG, Genres G
					       WHERE BA.band_id = BG.band_id
  					       AND BG.genre_id = G.genre_id
  					       AND G.genre LIKE 'Indie rock');

SELECT DISTINCT BE.artist_name     --1
FROM Belongs BE , Bands_Average
WHERE BE.band_id = Bands_Average.band_id AND  Bands_Average.avg_lenght = (SELECT MAX(Bands_Average.avg_lenght)        FROM Bands_Average);  --2

--Legenda:
--1:Gets the names of artists who belonged/belong to the winning band
--2:Gets the band_id of the indie rock band with the biggest average of album lenght
--3:Gets the band_id | avg_lenght of all indie rock bands as Bands_Average
--4:Gets the band_id of Indie Rock Bands



--Query2: Which musical genre has the most albuns in each decade?


SELECT Ranking.decade AS "Decade", Ranking.genre AS "Genre", Ranking.album_nr AS "Album_nr"   --3
FROM (SELECT Decade_Genre.decade AS decade, Decade_Genre.genre AS genre,   --2
	RANK() OVER (PARTITION BY Decade_Genre.decade ORDER BY Decade_Genre.album_nr DESC) album_rank, Decade_Genre.album_nr as album_nr
	FROM (SELECT (EXTRACT (DECADE FROM A.release)) AS decade, G.genre AS genre, COUNT(A.album_id) AS album_nr  --1
		FROM Albums A, Bands BA, Bands_Genres BG, Genres G
		WHERE A.band_id = BA.band_id
 		AND BA.band_id = BG.band_id
 		AND BG.genre_id = G.genre_id
		GROUP BY (EXTRACT (DECADE FROM A.release)), G.genre
		ORDER BY (EXTRACT (DECADE FROM A.release)) ) AS Decade_Genre)  AS Ranking
WHERE Ranking.album_rank = 1;


--Legenda:
--1:Cria uma tabela Decade_Genre com decada|genero|numero de albuns desse genero nessa decada
--2:Cria uma tabela Ranking com decada|genero|album_rank, onde cada decada tem o seu proprio ranking
--3:Seleciona a decada e o genero das entradas da tabela Ranking nas quais o ranking é 1 (ou seja, o genero com mais albuns nessa decada)
