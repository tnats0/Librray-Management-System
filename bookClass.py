import DataStorage.handleData as hData

class Book:

    def __init__(self,title,author,publisher,isbn):
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
            "publishers":self.publisher
        }

        return bookDict 


class Shelf:

    def __init__(self,name:str,books:list[Book],filter:dict=None):
        self.name = name
        self.books = books
        self.filter = filter

    def __repr__(self):

        return f"{self.__dir__}"


    def addToShelf(self,book:Book):

        self.books.append(book)

    def removeFromShelf(self,book:Book):

        self.books.remove(book)

