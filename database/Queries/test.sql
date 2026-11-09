
BEGIN;

SELECT * FROM shelves;

SELECT books.title,books.authors,books.publisher FROM books INNER JOIN shelf_books ON shelf_books.isbn = books.isbn WHERE shelf_id = 6;

ROLLBACK;

COMMIT;