SELECT * FROM books;
SELECT * FROM favorites;



CREATE TABLE favorites(

    isbn char(13) UNIQUE,
    title varchar(255) NOT NULL,
    authors VARCHAR(255) NOT NULL,
    publisher VARCHAR(255) NOT NULL

);

