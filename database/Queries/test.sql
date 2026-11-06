
BEGIN;

SELECT * FROM shelves;
SELECT * FROM books;

SELECT * FROM shelf_books;

INSERT INTO shelves (shelf_name) VALUES ('TEST');



ROLLBACK;

COMMIT;