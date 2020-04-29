# Напишете заявка, която за всеки кораб извежда името му, 
# държавата, броя оръдия и годината на пускане (launched)
SELECT s.name, c.country, c.numguns, s.launched 
  FROM ships AS s 
  JOIN classes AS c ON c.class = s.class; 

# Повторете горната заявка като този път включите в 
# резултата и класовете, които нямат кораби, но съществуват кораби 
# със същото име като тяхното.
SELECT cl.class  
  FROM classes AS cl
  LEFT OUTER JOIN ships AS sh ON sh.class = cl.class
  WHERE sh.name IS NULL; 

# + първата заявка
SELECT sh.name, cl.class, cl.country, cl.numguns, sh.launched   
  FROM classes AS cl 
  LEFT OUTER JOIN ships AS sh ON sh.class = cl.class 
  WHERE sh.name IS NULL 
  UNION 
  SELECT s.name, c.class, c.country, c.numguns, s.launched 
    FROM ships AS s  
    JOIN classes AS c ON c.class = s.class;

 # Напишете заявка, която извежда имената на корабите, 
 # участвали в битка от 1942г.
SELECT sh.name 
  FROM ships AS sh 
  JOIN outcomes AS o ON sh.name = o.ship 
  JOIN battles AS b ON b.name = o.battle 
  WHERE b.date LIKE '1942%';

#За всяка страна изведете имената на корабите, които никога не са участвали в битка.
SELECT sh.name 
  FROM ships AS sh
  LEFT OUTER JOIN outcomes AS o ON sh.name = o.ship 
  WHERE o.ship IS NULL; 