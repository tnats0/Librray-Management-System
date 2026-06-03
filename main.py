from handleData import *
from recoverData import *

import dotenv
import os

dotenv.load_dotenv(".env")

API_KEY = os.getenv("API_KEY")


# TODO: Some isbn codes stil cant be fetched info. 


def menu(isbn):

    try:

        book = find_book(isbn,API_KEY)

        append_book_data(book)

    except:

        print("Process Failed :(")


def test():

    with open("isbnCodes.txt","r") as file:

        codes = file.readlines()

        for code in codes:
            print(code,end="")
            menu(code)

    display_book_table()

test()