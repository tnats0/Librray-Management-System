import database.pool as pool
import bookClass as bcs
import DataStorage.handleData as hd


def create_shelf(shelf_name:str):

    command = "INSERT INTO shelves (shelf_name) VALUES (%s);"

    with pool.get_cursor() as cur:

        cur.execute(command,[shelf_name])


def add_book_to_shelf(isbn:str,shelf_id):

    command = "INSERT INTO shelf_books (isbn,shelf_id) VALUES (%s,%s);"

    with pool.get_cursor() as cur:

        cur.execute(command,[isbn,shelf_id])
        

def remove_book_from_shelf(isbn:str,shelf_id):

    command = "DELETE FROM shelf_books WHERE isbn = %s AND shelf_id = %s;"

    with pool.get_cursor() as cur:

        cur.execute(command,[isbn,shelf_id])

    
def delete_shelf(shelf_id):

    command = "DELETE FROM shelves WHERE shelf_id = (%s);"

    with pool.get_cursor() as cur:

        cur.execute(command,[shelf_id])

    
def get_shelf_data(shelf_id):

    command = "SELECT * FROM shelves WHERE shelf_id = %s;"

    with pool.get_cursor() as cur:

        cur.execute(command,[shelf_id])

        return cur.fetchall()

def get_shelf_books(shelf_id):

    command = """SELECT books.title,books.authors,books.publisher,books.isbn FROM books INNER JOIN shelf_books ON
    shelf_books.isbn = books.isbn WHERE shelf_id = %s;"""

    with pool.get_cursor() as cur:

        cur.execute(command,[shelf_id])

        return cur.fetchall()


def get_shelf_id(shelf_name):

    command = "SELECT shelf_id FROM shelves WHERE shelf_name LIKE %s LIMIT 1;"

    with pool.get_cursor() as cur:

        cur.execute(command,[shelf_name])

        return cur.fetchone()[0]
    

def turn_into_shelf(shelf_name):

    shelf_id = get_shelf_id(shelf_name)

    shelf_books = get_shelf_books(shelf_id)

    for i in range(len(shelf_books)):

        shelf_books[i] = hd.turn_into_book(shelf_books[i])
    

    shelf = bcs.Shelf(shelf_id,shelf_name,shelf_books)


    return shelf
    
