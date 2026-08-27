from requests import *
import json
import dotenv as denv
import os

denv.load_dotenv(".env")

key = os.getenv("api_key")

BASE_URL = "https://www.googleapis.com/books/v1/volumes"


def get_url(isbn:str,key=None):

    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={key}"

    return url

def get_volume_url(volumeId:str,key=None):

    url = f"https://www.googleapis.com/books/v1/volumes/{volumeId}?key={key}"

    return url

def get_info(url:str):

    data = Session().get(url).json()

    return data


def get_volumeId(url:str):
    
    data = Session().get(url).json()

    print(data)

    volumeId = data["items"][0]["id"]

    print(volumeId)

    return volumeId


def extract_from_googleBooks(info:dict): 

    print("Extracting...")
    
    extractedInfo = info["volumeInfo"]

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



def find_book(isbn:str,key=None):

    url = get_url(isbn,key)

    print(url)

    vid = get_volumeId(url)

    vurl = get_volume_url(vid,key)

    print(vurl)

    data = get_info(vurl)

    print(data)

    info = extract_from_googleBooks(data)

    return info



