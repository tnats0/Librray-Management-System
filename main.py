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

    print(turn_into_book(get_book("Metro 2033")[0]))

test()

