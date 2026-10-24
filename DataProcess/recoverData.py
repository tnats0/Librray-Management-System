from requests import *
import time


def get_volumeId(isbn:str,key=None):

    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={key}"

    req = Session().get(url)

    status = req.status_code

    print(f"Status Code: {status}")

    if status == 503:
        return status

    data = req.json()

    print(f"Sonuç : {data}")


    volumeId = data["items"][0]["id"]


    return volumeId

def get_data(volumeId:str,key=None):

    volume_url = f"https://www.googleapis.com/books/v1/volumes/{volumeId}?key={key}"

    req = Session().get(volume_url)

    status = req.status_code

    print(f"Status Code: {status}")

    if status == 503:
        return status

    data = req.json()

    print(f"Sonuç : {data}")


    return data


def extract_data(info:dict): 

    print("Extracting...")
    
    extractedInfo = info["volumeInfo"]

    try:
        title = extractedInfo["title"] if extractedInfo["title"] else "Unknown" 
        authors = extractedInfo["authors"][0] if extractedInfo["authors"][0] else "Unknown"
        publisher = extractedInfo["publisher"] if extractedInfo["publisher"] else "Unknown"
        

    except:
        authors = "Unknown"

    bookInfo = {

        "title": title,
        "author": authors,
        "publisher": publisher,
        "isbn": extractedInfo["industryIdentifiers"][1]["identifier"]

    }

    return bookInfo



def find_book(isbn:str,key=None):

    volumeId = get_volumeId(isbn,key)

    if volumeId == 503:
        return volumeId

    time.sleep(5)

    data = get_data(volumeId,key)

    if data == 503:
        return data

    print("Search Succeded!")

    info = extract_data(data)

    print("Extraction Succeded!")
    
    return info
