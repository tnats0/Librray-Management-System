import mysql.connector as sql
import dotenv as denv
import os
from bookClass import Book,Shelf

from database.pool import get_cursor


def append_book_data(bookData:dict,location="books"):


    appendCommand = f"INSERT {location} VALUES(%s,%s,%s,%s);"

    values = [location,bookData["isbn"],bookData["title"],bookData["authors"],bookData["publisher"]]

    with get_cursor(commit=True) as cur:

        cur.execute(appendCommand,values)


def turn_into_shelf(name,books:tuple):

    books = list(books)

    shelf = Shelf(name,books)

    return shelf

def get_shelf_data(shelf_name="books"):

    displayCommand = f"SELECT * from {shelf_name};"

    with get_cursor() as cursor:

        cursor.execute(displayCommand)

        return list(cursor.fetchall()) 

def get_shelf(shelf_name="books")->Shelf:

    shelf_data = get_shelf_data(shelf_name)

    shelf = turn_into_shelf(shelf_name,shelf_data)

    return shelf



def get_book(title,shelf="books"):


    command = "SELECT * FROM %s WHERE title = %s;"

    with get_cursor() as cur:

        cur.execute(command,[shelf,title])

        return cur.fetchall()




def turn_into_book(book_data:tuple):

    book = Book(book_data[0],book_data[1],book_data[2],book_data[3])

    return book




def check_data(isbn):

    command = "SELECT * FROM books WHERE isbn = %s LIMIT 1"
    
    with get_cursor() as cur:

        cur.execute(command,[isbn])

        isAvaliable = cur.fetchall()

    return 1 if isAvaliable else 0


