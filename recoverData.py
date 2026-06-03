from requests import *
import json
import dotenv as denv
import os

denv.load_dotenv(".env")

key = os.getenv("api_key")


def get_url(isbn:str,key):

    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={key}"

    return url


def get_info(url:str):
    
    data = get(url)

    info = data.json()

    return info 


def extract_info(info:dict): 
    
    extractedInfo = info["items"][0]["volumeInfo"]

    try:
        publisher = extractedInfo["publisher"]
    except:
        publisher = "Unknown"

    bookInfo = {

        "title": extractedInfo["title"],
        "author": extractedInfo["authors"][0],
        "publisher": publisher,
        "isbn": extractedInfo["industryIdentifiers"][1]["identifier"]

    }

    return bookInfo


def find_book(isbn:str,key):

    url = get_url(isbn,key)

    data = get_info(url)

    info = extract_info(data)

    return info


# result = find_book("9786254052033",key)
# result = json.dumps(result,indent=5)
# print(result)

