from rich.table import Table
from rich.console import Console
from DataStorage.handleData import *
from bookClass import *


console = Console()


def display(shelf:Shelf):

    books = shelf.books

    totalBooks = len(books)

    table = Table(title=f"Books In The Library ({totalBooks})")

    table.add_column("Number")
    table.add_column("Title")
    table.add_column("Author")
    table.add_column("Publishers")
    table.add_column("ISBN")

    for i,book in enumerate(books):

        table.add_row(str(i+1),book.title,book.author,book.publisher,book.isbn)

    console.print(table)
    




        