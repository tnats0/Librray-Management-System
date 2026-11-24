from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from DataStorage.handleData import search_books_by_term
from DataStorage.shelves import turn_into_shelf
from bookClass import Shelf

console = Console()

def display_books(shelf: Shelf) -> Panel:
    """Displays books for a given shelf in a rich Panel."""
    books = shelf.books
    totalBooks = len(books)
    
    table = Table(title=f"Books In {shelf.name} ({totalBooks})")

    table.add_column("Number")
    table.add_column("Title")
    table.add_column("Author")
    table.add_column("Publisher")
    table.add_column("ISBN")

    for i, book in enumerate(books):
        table.add_row(str(i+1), book.title, book.author, book.publisher, book.isbn)
    
    return Panel(table, title=f"Shelf: {shelf.name}")

def run_cli(shelf: Shelf):
    """Main interactive CLI loop."""
    console = Console()
    console.print(Panel(f"[bold cyan]Welcome to LibraryOS CLI[/bold cyan]", title="LibraryOS"))
    console.print(display_books(shelf))

    while True:
        console.print("\n[bold green]--- Menu ---[/bold green]")
        console.print("1. Add Book by ISBN")
        console.print("2. View Shelf Books")
        console.print("3. Change Shelf")
        console.print("4. Search Books (by Title/Author)")
        console.print("5. Exit")
        
        choice = Prompt.ask("[bold]Select an option[/bold] (1-5)")

        if choice == "1":
            isbn = Prompt.ask("Enter ISBN")
            # TODO: Implement logic to call add(isbn) from main.py context
            console.print(f"[yellow]Attempting to add book with ISBN: {isbn}. Requires integration with main.py logic.[/yellow]")
        elif choice == "2":
            console.print(display_books(shelf))
        elif choice == "3":
            shelf_name = Prompt.ask("Enter new shelf name")
            try:
                new_shelf = turn_into_shelf(shelf_name)
                shelf = new_shelf
                console.print(f"[yellow]Switched to shelf: {shelf.name}[/yellow]")
            except Exception as e:
                console.print(f"[red]Error changing shelf: {e}[/red]")
        elif choice == "4":
            search_term = Prompt.ask("Enter search term (Title/Author)")
            try:
                results = search_books_by_term(search_term)
                if not results:
                    console.print("[red]No books found matching your search.[/red]")
                else:
                    # Display results in a simple table or list
                    results_table = Table(title=f"Search Results for '{search_term}'")
                    results_table.add_column("Number")
                    results_table.add_column("Title")
                    results_table.add_column("Author")
                    results_table.add_column("ISBN")
                    
                    for i, book_data in enumerate(results):
                        results_table.add_row(str(i+1), book_data[1], book_data[2], book_data[3])
                    
                    console.print(results_table)
            except Exception as e:
                console.print(f"[red]Error during search: {e}[/red]")
        elif choice == "5":
            console.print("[bold red]Exiting CLI. Goodbye![/bold red]")
            break
        else:
            console.print("[red]Invalid choice. Please try again.[/red]")