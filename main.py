from DataStorage.handleData import *
from DataProcess.recoverData import *
from UI.terminal import *
import time
import random

import dotenv
import os

dotenv.load_dotenv(".env",override=True)

API_KEY = os.getenv("API_KEY")

def add(code):
    
    if check_data(code):
                
        print("Book is already in library")

    else:
        print("Book not found. Searching...")

        result = find_book(code,API_KEY)

        while result == 503:

            result = find_book(code,API_KEY)
            time.sleep(random.randint(1,5))
            print("Requesting again")

        isbn = input("ISBN: ")

        try:

                print("Inserting the book to the database...")

                append_book_data(result)

                print("Book has successfuly inserted!")

        except:

                print(f"Operation failed :( : {result}")

                time.sleep(random.randint(1,5))



def menu():
     
     code = input("ISBN: ")

     add(code)



display()
