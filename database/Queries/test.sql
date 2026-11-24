
BEGIN;

SELECT * FROM shelves;

SELECT * FROM shelf_books;

INSERT INTO shelves (shelf_name) VALUES
('Default Collection')

ROLLBACK;

COMMIT;