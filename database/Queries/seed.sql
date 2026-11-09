-- Test data for Library Management System
-- Run this AFTER database/Queries/init.sql
-- NOTE: Ensure column names match your schema (init.sql uses 'publishers', handleData.py uses 'publisher')

-- ============================================
-- Sample books
-- ============================================
INSERT INTO books (isbn, title, authors, publisher) VALUES
('9780132350884', 'Clean Code: A Handbook of Agile Software Craftsmanship', 'Robert C. Martin', 'Prentice Hall'),
('9780201633610', 'Design Patterns: Elements of Reusable Object-Oriented Software', 'Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides', 'Addison-Wesley'),
('9780131103627', 'The C Programming Language', 'Brian W. Kernighan, Dennis M. Ritchie', 'Prentice Hall'),
('9780596009205', 'Head First Design Patterns', 'Eric Freeman, Elisabeth Robson, Bert Bates, Kathy Sierra', "O'Reilly Media"),
('9780134685991', 'Effective Java', 'Joshua Bloch', 'Addison-Wesley'),
('9780132350815', 'Code Complete: A Practical Handbook of Software Construction', 'Steve McConnell', 'Microsoft Press'),
('9780134494166', 'Introduction to Algorithms', 'Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein', 'MIT Press'),
('9780132350838', 'Refactoring: Improving the Design of Existing Code', 'Martin Fowler', 'Addison-Wesley'),
('9780321125217', 'Domain-Driven Design: Tackling Complexity in the Heart of Software', 'Eric Evans', 'Addison-Wesley'),
('9780321356680', 'The Pragmatic Programmer: Your Journey to Mastery', 'Andrew Hunt, David Thomas', 'Addison-Wesley'),
('9780201485677', 'The Mythical Man-Month: Essays on Software Engineering', 'Frederick P. Brooks Jr.', 'Addison-Wesley'),
('9780134494258', 'Patterns of Enterprise Application Architecture', 'Martin Fowler', 'Addison-Wesley'),
('9780321334878', 'Working Effectively with Legacy Code', 'Michael C. Feathers', 'Prentice Hall'),
('9780132350891', 'Agile Software Development, Principles, Patterns, and Practices', 'Robert C. Martin', 'Prentice Hall'),
('9780321146533', 'UML Distilled: A Brief Guide to the Standard Object Modeling Language', 'Martin Fowler', 'Addison-Wesley'),
('9780201616224', 'Large-Scale C++ Software Design', 'John Lakos', 'Addison-Wesley'),
('9780131177053', 'Test Driven Development: By Example', 'Kent Beck', 'Addison-Wesley'),
('9780321146533', 'Clean Architecture: A Craftsman\'s Guide to Software Structure and Design', 'Robert C. Martin', 'Prentice Hall'),
('9780134685984', 'Python Crash Course', 'Eric Matthes', 'No Starch Press'),
('9781491919518', 'Fluent Python: Clear, Concise, and Effective Programming', 'Luciano Ramalho', "O'Reilly Media"),
('9780596517748', 'Python Cookbook', 'David Beazley, Brian K. Jones', "O'Reilly Media"),
('9780134692883', 'JavaScript: The Good Parts', 'Douglas Crockford', "O'Reilly Media"),
('9780321835203', 'HTML and CSS: Design and Build Websites', 'Jon Duckett', 'Wiley'),
('9780596007126', 'Learning Python', 'Mark Lutz', "O'Reilly Media");

-- ============================================
-- Sample custom shelves
-- ============================================
INSERT INTO shelves (shelf_name) VALUES
('Favorites'),
('To Read'),
('Science Fiction'),
('Classics');

-- ============================================
-- Associate books with shelves (shelf_books)
-- ============================================
-- Shelf 1 = Favorites
INSERT INTO shelf_books (shelf_id, isbn) VALUES
(5, '9780132350884'),
(5, '9780201633610');

-- Shelf 2 = To Read
INSERT INTO shelf_books (shelf_id, isbn) VALUES
(6, '9780596009205'),
(6, '9780134685991');

-- Shelf 3 = Science Fiction
INSERT INTO shelf_books (shelf_id, isbn) VALUES
(7, '9780131103627');

-- Shelf 4 = Classics
INSERT INTO shelf_books (shelf_id, isbn) VALUES
(8, '9780131103627');

-- ============================================
-- Sample favorites table entries
-- ============================================

-- ============================================
-- Verification queries (optional)
-- ============================================
-- SELECT * FROM books;
-- SELECT * FROM shelves;
-- SELECT * FROM shelf_books;
-- SELECT * FROM favorites;