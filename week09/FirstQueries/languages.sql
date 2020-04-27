CREATE TABLE Languages(
  id INTEGER PRIMARY KEY,
  language VARCHAR(20),
  answer VARCHAR(20),
  answered BOOL,
  guide TEXT
);
	

INSERT INTO Languages
  VALUES (1, 'Python', 'google', FALSE, 'A folder named Python was created. Go there and fight with program.py!');
  
INSERT INTO Languages
  VALUES (2, 'Go', '200 OK', FALSE, 'A folder named Go was created. Go there and try to make Google Go run.');
  
INSERT INTO Languages
  VALUES (3, 'Java', 'object oriented programming', FALSE, 'A folder named Java was created.
          Can you handle the class?');
  
INSERT INTO Languages
  VALUES (4, 'Haskell', 'Lambda', FALSE, 'Something pure has landed. Go to Haskell folder and see it!');
  
INSERT INTO Languages
  VALUES (5, 'C#', 'NDI=', FALSE, 'Do you see sharp? Go to the C# folder and check out.');
  
INSERT INTO Languages
  VALUES (6, 'Ruby', 'https://www.ruby-lang.org/bg/', FALSE, 'Ruby, ruby, rubyyy, aaahaaaahaa! (music). Go to Ruby folder!');
  
INSERT INTO Languages
  VALUES (7, 'C++', 'header files', FALSE, 'Here be dragons! It\'s C++ time. Go to the C++ folder.');

INSERT INTO Languages
  VALUES (8, 'JavaScript', 'Douglas Crockford', FALSE, 'NodeJS time. Go to JavaScript folder and Node your way!');



 ALTER TABLE Languages
  ADD COLUMN rating INTEGER CHECK (rating > 1 AND rating < 9);

UPDATE Languages
  SET rating = 1
  WHERE language = 'Python';

UPDATE Languages
  SET rating = 6
  WHERE language = 'Go';
  
UPDATE Languages
  SET rating = 5
  WHERE language = 'Java';
  
UPDATE Languages
  SET rating = 3
  WHERE language = 'Haskell';
  
UPDATE Languages
  SET rating = 4
  WHERE language = 'Ruby';
  
UPDATE Languages
  SET rating = 2
  WHERE language = 'C++';
  
UPDATE Languages
  SET rating = 7
  WHERE language = 'C#';
  
  
UPDATE Languages
  SET rating = 9
  WHERE language = 'JavaScript';


UPDATE Languages
  SET answered = True
  WHERE language = 'Python';
  
  
UPDATE Languages
  SET answered = True
  WHERE language = 'Go';

SELECT language
  FROM Languages
  where answer = '200 OK' Or answer = 'Lambda'