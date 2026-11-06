CREATE TABLE books(

    isbn CHAR(13) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    authors VARCHAR(255) NOT NULL,
    publisher VARCHAR(255) NOT NULL,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
);

CREATE TABLE shelves(

    shelf_id int AUTO_INCREMENT UNIQUE,
    shelf_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE shelf_books(

    shelf_id INT NOT NULL,
    isbn CHAR(13) NOT NULL,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,


    PRIMARY KEY (shelf_id,isbn),

    Foreign Key (shelf_id) REFERENCES shelves(shelf_id) ON DELETE CASCADE,
    Foreign Key (isbn) REFERENCES books(isbn) ON DELETE CASCADE

);

