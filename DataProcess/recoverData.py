from requests import *
import json
import dotenv as denv
import os
import asyncio as aio

denv.load_dotenv(".env")

key = os.getenv("api_key")


def set_url(isbn:str,key=None):

    if key:

        url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={key}" 

    else:

        url = f"https://openlibrary.org/isbn/{isbn}.json"

    return url


def get_info(url):
    
    data = get(url,"title")
    info = data.json()

    return info 

    
def extract_from_googleBooks(info:dict): 

    print("By GoogleBooks")
    
    extractedInfo = info["items"][0]["volumeInfo"]

    publisher = extractedInfo["publisher"]

    bookInfo = {

        "title": extractedInfo["title"],
        "authors": extractedInfo["authors"][0],
        "publisher": publisher,
        "isbn": extractedInfo["industryIdentifiers"][1]["identifier"]

    }

    return bookInfo

def get_from_googleBooks(isbn:str,key:str=None):

    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={key}" 

    info = get_info(url)

    result = extract_from_googleBooks(info)

    return result



def extract_from_openLibary(info:dict):

    print("By OpenLibrary")

    authorKey = info["authors"][0]["key"]

    authorURL = f"https://openlibrary.org/{authorKey}.json"

    print(authorURL)

    try:
        authorInfo = get_info(authorURL)["personal_name"]

    except: 
        authorInfo = "Unknown"        

    bookInfo = {

        "title":info["title"],
        "authors":authorInfo,
        "publishers":info["publishers"][0],
        "isbn":info["isbn_13"][0]
        
        }


    return bookInfo



def get_from_openLibrary(isbn:str):

    url = f"https://openlibrary.org/isbn/{isbn}.json"

    info = get_info(url)

    result = extract_from_openLibary(info)

    return result



def extract_from_user():

    bookInfo = {

        "title":"",
        "author":"", 
        "publisher":"", 
        "isbn":""
    }

    for i in bookInfo.keys():

        info = input(f"{i}: ")

        bookInfo[i] = info

    return bookInfo



def find_book(isbn:str,key=None):

    try:

        result = get_from_googleBooks(isbn,key)

    except:

        result = get_from_openLibrary(isbn)

    else:

        raise Exception("Kitap bulunamadı :(")

    return result



