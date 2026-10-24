import mysql.connector as sql
import dotenv as denv
import os
from bookClass import Book

from database.pool import get_cursor



def append_book_data(bookData:dict):


    appendCommand = "INSERT books VALUES(%s,%s,%s,%s);"

    values = [bookData["title"],bookData["author"],bookData["publisher"],bookData["isbn"]]

    with get_cursor() as cur:

        cur.execute(appendCommand,values)



def display_book_table():

    displayCommand = "SELECT * from books;"

    with get_cursor() as cursor:

        cursor.execute(displayCommand)

    return cursor.fetchall() 




def get_book(title):


    command = "SELECT * FROM books WHERE title = %s;"

    with get_cursor() as cur:

        cur.execute(command,[title])

        return cur.fetchall()

    

def turn_into_book(book_data:tuple):

    book = Book(book_data[0],book_data[1],book_data[2],book_data[3])

    return book

def check_data(isbn):

    command = "SELECT * FROM books WHERE isbn = %s LIMIT 1"
    
    with get_cursor as cur:

        cur.execute(command,[isbn])

        isAvaliable = cur.fetchall()

    return 1 if isAvaliable else 0


