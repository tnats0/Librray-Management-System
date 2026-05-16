from requests import *



def get_url(isbn:str):

    url = f"https://openlibrary.org/isbn/{isbn}.json"


    return url


def get_info(url:str):
    
    data = get(url,"title")

    info = data.json()

    return info


def extract_info(info:dict): 
    

    authorKey = info["authors"][0]["key"]

    authorURL = f"https://openlibrary.org/{authorKey}.json"

    try:
        authorInfo = get_info(authorURL)["personal_name"]
    except: authorInfo = "Unknown"


    extractedInfo = {"title":info["title"],"authors":authorInfo,"publishers":info["publishers"][0],"isbn":info["isbn_13"][0]}


    return list(extractedInfo.values())


def find_book(isbn:str):

    url = get_url(isbn)

    data = get_info(url)

    info = extract_info(data)

    return info

