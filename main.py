from DataStorage.handleData import *
from DataProcess.recoverData import *

import dotenv
import os

dotenv.load_dotenv(".env")

API_KEY = os.getenv("API_KEY")


def menu():
        
    while True:

        isbn = input("ISBN: ")

        book = find_book(isbn,API_KEY)

        
        append_book_data(book)
        print("Added to the Library")





menu()
