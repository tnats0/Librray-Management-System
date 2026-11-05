import fastapi
from DataStorage.handleData import *
from DataProcess.recoverData import *

app = fastapi.FastAPI()

@app.get("/books")
async def show_books():

    result = get_shelf_data()

    return result

@app.post("/books/new/{isbn:str}")
async def add_books(isbn:str):
        
    data = find_book(isbn)
    append_book_data(data)
