import mysql.connector as sql




def connect():

    global connection 
    connection = sql.connect(host="127.0.0.1",user="root",password="root123",database="libraryDatabase",autocommit=True)

    global cursor 
    cursor = connection.cursor()

def disconnect():
    cursor.close()
    connection.close()
    

def append_book_data(bookData:dict):

    appendCommand = f"INSERT books VALUES('{bookData[0]}','{bookData[1]}','{bookData[2]}','{bookData[3]}');"

    cursor.execute(appendCommand)

def display_book_table():

    displayCommand = "SELECT * from books;"

    cursor.execute(displayCommand)

    table = []

    for i,data in enumerate(cursor):

        print(f"> {i}. - {data}")
        table.append(data)


    return table







