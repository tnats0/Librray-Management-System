from DataStorage.handleData import *
from DataProcess.recoverData import *
from UI.terminal import *
import time
import random

import dotenv
import os

dotenv.load_dotenv(".env")

API_KEY = os.getenv("API_KEY")

def loop():

    with open("C:\\Users\\TARIK ATASOY\\projects\\helloworld\\Projects\\Library_Management_System\\codes.txt","r",encoding="utf-8") as file:

        codes = file.read().split("\n")

        codes.pop()

        print(codes)

        for code in codes:

            print(f"Searching {code} ...")

            result = find_book(code,API_KEY)

            try:

                append_book_data(result)

            except:

                print("---")

            time.sleep(random.randint(1,5))
            



display()

isbn = "9786053607021"

# result = find_book(isbn,API_KEY)

# print(result)

# append_book_data(result)