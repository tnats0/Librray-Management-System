import mysql.connector as sql
import dotenv as denv
import os
from bookClass import Book

denv.load_dotenv(".env")

user=os.getenv("DBUserName")
password=os.getenv("DBPassword")
database=os.getenv("DBName")

def connect():
    return sql.connect(host="127.0.0.1",username=user,password=password,database=database)


def append_book_data(bookData:dict):

    connection = connect()
    cursor = connection.cursor()

    appendCommand = f"INSERT books VALUES('{bookData["title"]}','{bookData["author"]}','{bookData["publisher"]}','{bookData["isbn"]}');"

    cursor.execute(appendCommand)
    connection.commit()

    cursor.close()
    connection.close()


def display_book_table():

    connection = connect()
    cursor = connection.cursor()

    displayCommand = "SELECT * from books;"

    cursor.execute(displayCommand)

    data = cursor.fetchall()

    cursor.close()
    connection.close()

    return data 


def get_book(title):

    connection = connect()
    cursor = connection.cursor()

    command = f"SELECT * FROM books WHERE title = '{title}';"

    cursor.execute(command)

    book = cursor.fetchall()

    cursor.close()
    connection.close()
    
    return book


def turn_into_book(book_data:tuple):

    book = Book(book_data[0],book_data[1],book_data[2],book_data[3])

    return book








