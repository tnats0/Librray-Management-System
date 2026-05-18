import mysql.connector as sql
import dotenv as denv
import os

denv.load_dotenv(".env")

def connect():

    user=os.getenv("DBUserName")
    password=os.getenv("DBPassword")
    database=os.getenv("DBName")

    global connection 
    connection = sql.connect(host="127.0.0.1",user=user,password=password,database=database,autocommit=True)

    global cursor 
    cursor = connection.cursor()

def disconnect():
    cursor.close()
    connection.close()
    

def append_book_data(bookData:dict):

    connect()

    appendCommand = f"INSERT books VALUES('{bookData[0]}','{bookData[1]}','{bookData[2]}','{bookData[3]}');"

    cursor.execute(appendCommand)

    disconnect()

def display_book_table():

    connect()

    displayCommand = "SELECT * from books;"

    cursor.execute(displayCommand)

    table = []

    for i,data in enumerate(cursor):

        print(f"> {i}. - {data}")
        table.append(data)


    return table

    disconnect()







