# First Queries

# Напишете заявка, която извежда адреса на студио ‘MGM’
SELECT address
  FROM STUDIO
  WHERE name = 'MGM';

# Напишете заявка, която извежда рождената дата на актрисата Kim Basinger
SELECT birthdate
  FRom MOVIESTAR
  WHERE name = 'Kim Basinger';

# Напишете заявка, която извежда имената всички продуценти
# на филми с нетни активи (networth) над 10 000 000 долара
SELECT name
  FROM MOVIEEXEC
  WHERE networth > 10000000;

#Напишете заявка, която извежда имената на всички актьори, 
# които са мъже или живеят на Prefect Rd
SELECT name 
  FROM MOVIESTAR
  WHERE gender = 'M' OR address = 'Prefect Rd';

# Добавате нова филмова звезда 'Zahari Baharov', с адрес и рожденна дата по ваш избор.
INSERT into MOVIESTAR
  VALUES ('Zahari Baharov', 'zk.Mladost', 'M', '1988-08-12');

# Изтрийте всички студия, които имат в адреса си числото 5.
DELETE FROM STUDIO
  WHERE address LIKE '%5%'

# Променете студио да бъде "Fox" на тези филми, които в имената си имат 'star.
UPDATE MOVIE
  SET studioname = 'Fox'
  WHERE title LIKE '%star%';

# Relations

# Напишете заявка, която извежда имената на актьорите мъже участвали в 
# ‘Terms of Endearment’
SELECT name
  FROM STARSIN
  JOIN MOVIESTAR ON STARSIN.starname = MOVIESTAR.name
  WHERE MOVIESTAR.gender = 'M' AND STARSIN.movietitle = 'Terms of Endearment'

# Напишете заявка, която извежда имената на актьорите участвали във 
# филми продуцирани от ‘MGM’през 1995 г.
SELECT STARSIN.STARNAME
  FROM STARSIN
  JOIN MOVIE ON MOVIE.TITLE = STARSIN.MOVIETITLE
  JOIN STUDIO ON MOVIE.studioname = STUDIO.NAME
  WHERE STUDIO.name = 'MGM' AND MOVIE.year = 1995

# Добавете колона "име на президент"на таблицата 
# Студио и съответно и задайте стойности.Напишете заявка, която извежда името на президента на ‘MGM’
ALTER TABLE STUDIO
  ADD COLUMN president varchar(20);

UPDATE STUDIO
  SET president = 'Ivan'
  WHERE name = 'MGM';

UPDATE STUDIO
  SET president = 'Pesho'
  WHERE name = 'USA Entertainm.';

SELECT president
  FROM STUDIO
  WHERE name = 'MGM'