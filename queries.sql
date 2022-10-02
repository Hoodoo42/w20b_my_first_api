INSERT INTO animal (name, species) VALUES ('German Shepard', 'Dog'), ('Dalmation', 'Dog'), ('Hound', 'Dog'), ('Savanna', 'Cat'), ('Siamese', 'Cat');

SELECT name, species FROM animal;
SELECT name, species FROM animal a WHERE a.species = 'Dog';
SELECT name, species FROM animal a WHERE a.species = 'Cat';
	