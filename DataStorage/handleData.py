import mysql.connector as sql
import dotenv as denv
import os

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

    table = []

    for data in cursor:

        book = {"title":data[0],"author":data[1],"publisher":data[2],"isbn":data[3]}

        table.append(book)

    cursor.close()
    connection.close()

    return table









