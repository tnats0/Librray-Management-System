from handleData import *
from recoverData import *


def menu(isbn):

    try:

        book = find_book(isbn)

        connect()

        append_book_data(book)

        display_book_table()

        disconnect()

    except: print("Process failed :(")


with open("isbn2.txt","r") as file:

    codes = file.readlines()

    for code in codes:
        print(code,end="")
        menu(code)

