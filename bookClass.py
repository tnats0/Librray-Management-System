import DataStorage.handleData as hData
import DataStorage.shelves as sData

class Book:

    def __init__(self,isbn,title,author,publisher):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.isbn = isbn

    def book(title):

        data = hData.get_book(title)

        book = Book(data[0],data[1],data[2],data[3])

        return book


    def __repr__(self):

        bookDict = {
            "isbn":self.isbn,
            "title":self.title,
            "authors":self.author,
            "publisher":self.publisher
        }

        return bookDict 


class Shelf:

    def __init__(self,id,name:str):
        self.id = id
        self.name = name
        self.books = None

    def __repr__(self):

        return self.__dict__()


    def addToShelf(self,book:Book):


        sData.add_book_to_shelf(book.isbn,self.id)

    def removeFromShelf(self,book:Book):
        pass


