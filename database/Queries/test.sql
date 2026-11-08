
BEGIN;

SELECT * FROM shelves;
SELECT * FROM books;

SELECT * FROM shelf_books;


ROLLBACK;

COMMIT;