from DataStorage.handleData import *
from DataProcess.recoverData import *

import dotenv
import os

dotenv.load_dotenv(".env")

API_KEY = os.getenv("API_KEY")


def menu(isbn):


    book = find_book(isbn,API_KEY)

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