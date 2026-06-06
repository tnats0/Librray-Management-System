from requests import *
import json
import dotenv as denv
import os

denv.load_dotenv(".env")

key = os.getenv("api_key")


def get_url(isbn:str,key=None):

    if key:

        url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={key}" 

    else:

        url = f"https://openlibrary.org/isbn/{isbn}.json"

    return url


def get_info(url:str):
    
    data = get(url,"title")

    info = data.json()

    return info 


def extract_from_googleBooks(info:dict): 
    
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

def extract_from_openLibary(info:dict):

    print("By OpenLibrary")

    authorKey = info["authors"][0]["key"]

    authorURL = f"https://openlibrary.org/{authorKey}.json"

    try:
        authorInfo = get_info(authorURL)["personal_name"]

    except: authorInfo = "Unknown"

    extractedInfo = {

        "title":info["title"],
        "authors":authorInfo,
        "publishers":info["publishers"][0],
        "isbn":info["isbn_13"][0]
        
        }


    return extractedInfo



def find_book(isbn:str,key=None):

    url = get_url(isbn,key)

    data = get_info(url)

    if key:

        info = extract_from_googleBooks(data)

    else:

        info = extract_from_openLibary(data)


    return info


