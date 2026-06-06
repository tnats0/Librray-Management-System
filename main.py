from handleData import *
from recoverData import *

import dotenv
import os

dotenv.load_dotenv(".env")

API_KEY = os.getenv("API_KEY")


def menu(isbn):

    try:

        book = find_book(isbn,API_KEY)

        print("Found! ")

    except:

        print("Searching Again...")

        try:

            book = find_book(isbn)

        except:

            print("Process Failed :(")

    
    else:
        try:
            append_book_data(book)
            print("Added to the Library")

        except: print("Already in Library")


def test():

    with open("isbnCodes.txt","r") as file:

        codes = file.readlines()

        for code in codes:
            print(code,end="")
            menu(code)


    display_book_table()

test()