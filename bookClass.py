class Book:

    def __init__(self,title,author,publisher,isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.isbn = isbn

    def __repr__(self):

        return f"{self.title} {self.author} {self.publisher} {self.isbn}"

    
