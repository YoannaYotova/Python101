# Напишете заявка, която извежда средната скорост на компютрите
SELECT AVG(speed)
  FROM pc;

# Напишете заявка, която извежда средния размер на екраните
# на лаптопите за всеки производител.
SELECT p.maker, AVG(l.screen) AS 'avg_screen'
  FROM laptop AS l
  JOIN product AS p ON l.model = p.model
  GROUP BY p.maker;

# Напишете заявка, която извежда средната
# скорост на лаптопите с цена над 1000.
SELECT price, AVG(speed) AS 'avg_speed'
  FROM laptop
  GROUP BY price
  HAVING price > 1000;

# Напишете заявка, която извежда 
# средната цена на компютрите според различните им hd.
SELECT hd, AVG(price) AS 'avg_price'
  FROM laptop
  GROUP BY hd;

# Напишете заявка, която извежда средната 
# цена на компютрите за всяка скорост по-голяма от 500.
SELECT speed, AVG(price) AS 'avg_price'
  FROM pc
  GROUP BY speed
  HAVING speed > 500;

# Напишете заявка, която извежда средната 
# цена на компютрите произведени от производител ‘A’.
SELECT maker, AVG(price) AS 'avg_price'
  FROM pc
  JOIN product AS p ON p.model = pc.model
  WHERE p.maker = 'A';

# Напишете заявка, която извежда средната 
# цена на компютрите и лаптопите за производител ‘B’
SELECT product.maker, AVG(data.price) AS 'avg_price' 
  FROM (SELECT * FROM laptop 
  	      UNION 
  	      SELECT * FROM pc) AS data 
  JOIN product ON product.model = data.model 
  GROUP BY product.maker 
  HAVING product.maker = 'B';

# Напишете заявка, която извежда производителите, 
# които са произвели поне по 3 различни модела компютъра. 
# Помислете каква заявка можете да напишете за да сте сигурни в отговора,
# например да изведете за всеки производител, броя различни модели компютри.
SELECT p.maker, COUNT(pc.model) AS 'models_count'
  FROM pc 
  JOIN product AS p ON p.model = pc.model 
  GROUP BY pc.model 
  HAVING COUNT(pc.model) > 3; 

# Напишете заявка, която извежда производителите на компютрите с най-висока цена.
SELECT p.maker 
  FROM product AS p 
  JOIN pc ON pc.model = p.model 
  WHERE pc.price = (SELECT MAX(price) 
         			  FROM pc); 

# Напишете заявка, която извежда средния размер на диска 
# на тези компютри произведени от производители, които произвеждат и принтери.
SELECT pc.model, AVG(hd) AS 'avg_hd' 
  FROM product AS p 
  JOIN pc ON p.model = pc.model 
  WHERE p.maker IN (SELECT maker 
  	                  FROM product 
  	                  WHERE type = 'Printer') 
  GROUP BY pc.model;