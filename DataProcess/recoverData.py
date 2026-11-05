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


def extract_data(info:dict,isbn:str): 

    print("Extracting...")
    
    extractedInfo = info["volumeInfo"]

    title,authors,publisher = "","",""

    bookInfo = {

        "title": "Unknown",
        "authors": "Unknown",
        "publisher": "Unknown",
        "isbn": isbn

    }

    try:

        title = extractedInfo["title"]
        bookInfo["title"] = title

    except KeyError:

        pass
    
    try:

        authors = extractedInfo["authors"][0]
        bookInfo["authors"] = authors

    except KeyError:

        pass


    try:

        publisher = extractedInfo["publisher"]
        bookInfo["publisher"] = publisher

    except KeyError:

        pass

    

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

    info = extract_data(data,isbn)

    print("Extraction Succeded!")
    
    return info
