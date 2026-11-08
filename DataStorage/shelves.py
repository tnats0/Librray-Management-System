import database.pool as pool
import bookClass as bcs
import DataStorage.handleData as hd


def create_shelf(shelf_name:str):

    command = "INSERT INTO shelves (shelf_name) VALUES (%s);"

    with pool.get_cursor() as cur:

        cur.execute(command,[shelf_name])


def add_book_to_shelf(isbn:str):

    command = "INSERT INTO shelf_books (isbn) VALUES (%s);"

    with pool.get_cursor() as cur:

        cur.execute(command,[isbn])
        

def remove_book_from_shelf(isbn:str):

    command = "DELETE FROM shelf_books WHERE isbn = %s;"

    with pool.get_cursor() as cur:

        cur.execute(command,[isbn])

    
def delete_shelf(shelf_name:str):

    command = "DELETE FROM shelves WHERE shelf_name = (%s);"

    with pool.get_cursor() as cur:

        cur.execute(command,[shelf_name])

    
def get_shelf_data(shelf_name:str):

    command = "SELECT * FROM shelves WHERE shelf_name = %s;"

    with pool.get_cursor() as cur:

        cur.execute(command,[shelf_name])
    